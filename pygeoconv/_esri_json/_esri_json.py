def esri_json_to_geojson(arcgis: dict, id_attribute=None):
    geojson = {}

    if 'features' in arcgis:
        geojson['type'] = 'FeatureCollection'
        geojson['features'] = []
        for feature in arcgis['features']:
            geojson['features'].append(esri_json_to_geojson(feature, id_attribute))

    if isinstance(arcgis.get('x'), (int, float)) and isinstance(arcgis.get('y'), (int, float)):
        geojson['type'] = 'Point'
        geojson['coordinates'] = [arcgis['x'], arcgis['y']]
        if isinstance(arcgis.get('z'), (int, float)):
            geojson['coordinates'].append(arcgis['z'])

    if 'points' in arcgis:
        geojson['type'] = 'MultiPoint'
        geojson['coordinates'] = arcgis['points'][:]

    if 'paths' in arcgis:
        if len(arcgis['paths']) == 1:
            geojson['type'] = 'LineString'
            geojson['coordinates'] = arcgis['paths'][0][:]
        else:
            geojson['type'] = 'MultiLineString'
            geojson['coordinates'] = arcgis['paths'][:]

    if 'rings' in arcgis:
        geojson = _convert_rings_to_geojson(arcgis['rings'][:])

    if all(key in arcgis and isinstance(arcgis[key], (int, float)) for key in ['xmin', 'ymin', 'xmax', 'ymax']):
        geojson['type'] = 'Polygon'
        geojson['coordinates'] = [[
            [arcgis['xmax'], arcgis['ymax']],
            [arcgis['xmin'], arcgis['ymax']],
            [arcgis['xmin'], arcgis['ymin']],
            [arcgis['xmax'], arcgis['ymin']],
            [arcgis['xmax'], arcgis['ymax']]
        ]]

    if 'geometry' in arcgis or 'attributes' in arcgis:
        geojson['type'] = 'Feature'
        geojson['geometry'] = esri_json_to_geojson(arcgis['geometry']) if 'geometry' in arcgis else None
        geojson['properties'] = arcgis['attributes'].copy() if 'attributes' in arcgis else {}
        if 'attributes' in arcgis:
            try:
                geojson['id'] = _get_id(arcgis['attributes'], id_attribute)
            except ValueError:
                pass

    if geojson.get('geometry') == {}:
        geojson['geometry'] = None

    return geojson


def _convert_rings_to_geojson(rings: list):
    outer_rings = []
    holes = []
    x = 0
    outer_ring = None
    hole = None

    for r in range(len(rings)):
        ring = _close_ring(rings[r][:])
        if len(ring) < 4:
            continue
        if _ring_is_clockwise(ring):
            polygon = [ring[::-1]]  # wind outer rings counterclockwise for RFC 7946 compliance
            outer_rings.append(polygon)
        else:
            holes.append(ring[::-1])  # wind inner rings clockwise for RFC 7946 compliance

    uncontained_holes = []

    while holes:
        hole = holes.pop()
        contained = False
        for x in range(len(outer_rings) - 1, -1, -1):
            outer_ring = outer_rings[x][0]
            if _coordinates_contain_coordinates(outer_ring, hole):
                outer_rings[x].append(hole)
                contained = True
                break
        if not contained:
            uncontained_holes.append(hole)

    while uncontained_holes:
        hole = uncontained_holes.pop()
        intersects = False
        for x in range(len(outer_rings) - 1, -1, -1):
            outer_ring = outer_rings[x][0]
            if _array_intersects_array(outer_ring, hole):
                outer_rings[x].append(hole)
                intersects = True
                break
        if not intersects:
            outer_rings.append([hole[::-1]])

    if len(outer_rings) == 1:
        return {
            'type': 'Polygon',
            'coordinates': outer_rings[0]
        }
    else:
        return {
            'type': 'MultiPolygon',
            'coordinates': outer_rings
        }


def _get_id(attributes: dict, id_attribute: str):
    keys = [id_attribute, 'OBJECTID', 'FID'] if id_attribute else ['OBJECTID', 'FID']
    for key in keys:
        if key in attributes and (isinstance(attributes[key], str) or isinstance(attributes[key], int)):
            return attributes[key]
    raise ValueError('No valid id attribute found')


def _coordinates_contain_point(coordinates: list, point: list):
    contains = False
    for i in range(-1, len(coordinates) - 1):
        if ((coordinates[i][1] <= point[1] < coordinates[i + 1][1]) or
            (coordinates[i + 1][1] <= point[1] < coordinates[i][1])) and \
                (point[0] < (coordinates[i + 1][0] - coordinates[i][0]) * (point[1] - coordinates[i][1]) /
                 (coordinates[i + 1][1] - coordinates[i][1]) + coordinates[i][0]):
            contains = not contains
    return contains


def _array_intersects_array(a: list, b: list):
    for i in range(len(a) - 1):
        for j in range(len(b) - 1):
            if _edge_intersects_edge(a[i], a[i + 1], b[j], b[j + 1]):
                return True
    return False


def _edge_intersects_edge(a1: list, a2: list, b1: list, b2: list):
    ua_t = (b2[0] - b1[0]) * (a1[1] - b1[1]) - (b2[1] - b1[1]) * (a1[0] - b1[0])
    ub_t = (a2[0] - a1[0]) * (a1[1] - b1[1]) - (a2[1] - a1[1]) * (a1[0] - b1[0])
    u_b = (b2[1] - b1[1]) * (a2[0] - a1[0]) - (b2[0] - b1[0]) * (a2[1] - a1[1])

    if u_b != 0:
        ua = ua_t / u_b
        ub = ub_t / u_b

        if 0 <= ua <= 1 and 0 <= ub <= 1:
            return True
    return False


def _coordinates_contain_coordinates(outer: list, inner: list):
    intersects = _array_intersects_array(outer, inner)
    contains = _coordinates_contain_point(outer, inner[0])
    if not intersects and contains:
        return True
    return False


def _close_ring(ring: list):
    if ring[0] != ring[-1]:
        ring.append(ring[0])
    return ring


def _ring_is_clockwise(ring: list):
    area = 0
    for i in range(len(ring)):
        j = (i + 1) % len(ring)
        area += (ring[j][0] - ring[i][0]) * (ring[j][1] + ring[i][1])
    return area >= 0
