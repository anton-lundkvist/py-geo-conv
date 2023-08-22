from pygeoconv.errors import EsriJsonParserError


def esri_json_to_geojson(arcgis: dict, id_attribute=None):
    geojson = dict()
    if 'features' in arcgis:
        geojson = _convert_feature_set(arcgis, id_attribute)

    elif "x" in arcgis and "y" in arcgis:
        geojson = convert_point(arcgis)

    elif 'points' in arcgis:
        geojson = _convert_multipoint(arcgis)

    elif 'paths' in arcgis:
        geojson = _convert_polyline(arcgis)

    elif 'rings' in arcgis:
        geojson = _convert_polygon(arcgis['rings'][:])

    elif all(key in arcgis for key in ['xmin', 'ymin', 'xmax', 'ymax']):
        geojson = _convert_extent(arcgis)

    elif 'geometry' in arcgis or 'attributes' in arcgis:
        geojson = _convert_feature(arcgis, id_attribute)

    if geojson.get('geometry') == {}:
        geojson.update({"geometry": None})
    if not geojson:
        raise EsriJsonParserError("Unable to parse Esri Json object, unknown object type")
    return geojson


def _convert_feature_set(arcgis: dict, id_attribute: str):
    geojson = {'type': 'FeatureCollection', 'features': []}
    for feature in arcgis['features']:
        geojson['features'].append(esri_json_to_geojson(feature, id_attribute))
    return geojson


def _convert_feature(arcgis: dict, id_attribute):
    geojson = {'type': 'Feature',
               'geometry': esri_json_to_geojson(arcgis['geometry']) if 'geometry' in arcgis else None,
               'properties': arcgis['attributes'].copy() if 'attributes' in arcgis else {}}
    if 'attributes' in arcgis:
        try:
            geojson['id'] = _get_id(arcgis['attributes'], id_attribute)
        except ValueError:
            pass
    return geojson


def convert_point(arcgis: dict):
    if arcgis.get("x") == "NaN" or arcgis.get("x") is None:
        return {'type': 'Point', 'coordinates': []}
    if not isinstance(arcgis.get('x'), (int, float)) and not isinstance(arcgis.get('y'), (int, float)):
        raise EsriJsonParserError(f"Invalid coordinates for type point, {arcgis.get('x'), arcgis.get('y')}")
    geojson = {'type': 'Point', 'coordinates': [arcgis['x'], arcgis['y']]}
    if isinstance(arcgis.get('z'), (int, float)):
        geojson['coordinates'].append(arcgis['z'])
    return geojson


def _convert_multipoint(arcgis: dict):
    return {'type': 'MultiPoint', 'coordinates': arcgis['points'][:]}


def _convert_polyline(arcgis: dict):
    geojson = {}
    if len(arcgis['paths']) == 1:
        geojson['type'] = 'LineString'
        geojson['coordinates'] = arcgis['paths'][0][:]
    else:
        geojson['type'] = 'MultiLineString'
        geojson['coordinates'] = arcgis['paths'][:]
    return geojson


def _convert_polygon(rings: list):
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


def _convert_extent(arcgis: dict):
    if arcgis.get("xmin") is None or arcgis.get("xmin") == "NaN":
        return {'type': 'Polygon', 'coordinates': []}
    if not all(isinstance(arcgis[key], (int, float)) for key in ['xmin', 'ymin', 'xmax', 'ymax']):
        raise EsriJsonParserError("Invalid coordinates for type Extent")
    geojson = {'type': 'Polygon', 'coordinates': [[
        [arcgis['xmax'], arcgis['ymax']],
        [arcgis['xmin'], arcgis['ymax']],
        [arcgis['xmin'], arcgis['ymin']],
        [arcgis['xmax'], arcgis['ymin']],
        [arcgis['xmax'], arcgis['ymax']]
    ]]}
    return geojson


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
