def geojson_to_arcgis(geojson, id_attribute='OBJECTID', wkid: int = 4326):
    result = {}

    if geojson['type'] == 'Point':
        result = parse_point(geojson, wkid)
    elif geojson['type'] == 'MultiPoint':
        result = parse_multi_point(geojson, wkid)
    elif geojson['type'] == 'LineString':
        result = parse_linestring(geojson, wkid)
    elif geojson['type'] == 'MultiLineString':
        result = parse_multi_linestring(geojson, wkid)
    elif geojson['type'] == 'Polygon':
        result = parse_polygon(geojson, wkid)
    elif geojson['type'] == 'MultiPolygon':
        result = parse_multi_polygon(geojson, wkid)
    elif geojson['type'] == 'Feature':
        result = parse_feature(geojson, id_attribute, wkid)
    elif geojson['type'] == 'FeatureCollection':
        result = parse_feature_collection(geojson, id_attribute, wkid)
    elif geojson['type'] == 'GeometryCollection':
        result = parse_geometry_collection(geojson, id_attribute, wkid)
    return result


def parse_point(geojson: dict, wkid: int):
    spatial_reference = {'wkid': wkid}
    result = {'x': geojson['coordinates'][0], 'y': geojson['coordinates'][1]}
    if len(geojson['coordinates']) > 2:
        result['z'] = geojson['coordinates'][2]
    result['spatialReference'] = spatial_reference
    return result


def parse_multi_point(geojson: dict, wkid: int):
    spatial_reference = {'wkid': wkid}
    result = {'points': geojson['coordinates'][:]}
    if len(geojson['coordinates'][0]) > 2:
        result['hasZ'] = True
    result['spatialReference'] = spatial_reference
    return result


def parse_linestring(geojson: dict, wkid: int):
    spatial_reference = {'wkid': wkid}
    result = {'paths': [geojson['coordinates'][:]]}
    if len(geojson['coordinates'][0]) > 2:
        result['hasZ'] = True
    result['spatialReference'] = spatial_reference
    return result


def parse_multi_linestring(geojson: dict, wkid: int):
    spatial_reference = {'wkid': wkid}
    result = {'paths': geojson['coordinates'][:]}
    if len(geojson['coordinates'][0][0]) > 2:
        result['hasZ'] = True
    result['spatialReference'] = spatial_reference
    return result


def parse_polygon(geojson: dict, wkid: int):
    spatial_reference = {'wkid': wkid}
    result = {'rings': _orient_rings(geojson['coordinates'][:])}
    if len(geojson['coordinates'][0][0]) > 2:
        result['hasZ'] = True
    result['spatialReference'] = spatial_reference
    return result


def parse_multi_polygon(geojson: dict, wkid: int):
    spatial_reference = {'wkid': wkid}
    result = {'rings': _flatten_multi_polygon_rings(geojson['coordinates'][:])}
    if len(geojson['coordinates'][0][0][0]) > 2:
        result['hasZ'] = True
    result['spatialReference'] = spatial_reference
    return result


def parse_feature(geojson: dict, id_attribute: str, wkid: int):
    result = {}
    if geojson.get("geometry"):
        result['geometry'] = geojson_to_arcgis(geojson['geometry'], id_attribute, wkid)
    result['attributes'] = _shallow_clone(geojson['properties']) if geojson['properties'] else {}
    if 'id' in geojson:
        result['attributes'][id_attribute] = geojson['id']
    return result


def parse_feature_collection(geojson: dict, id_attribute: str, wkid: int):
    result = []
    for feature in geojson['features']:
        result.append(geojson_to_arcgis(feature, id_attribute, wkid))
    return result


def parse_geometry_collection(geojson: dict, id_attribute: str, wkid: int):
    result = []
    for geometry in geojson['geometries']:
        result.append(geojson_to_arcgis(geometry, id_attribute, wkid))
    return result


def _shallow_clone(obj):
    target = {}
    for key, value in obj.items():
        target[key] = value
    return target


def _flatten_multi_polygon_rings(rings):
    output = []
    for i in range(len(rings)):
        polygon = _orient_rings(rings[i])
        for x in range(len(polygon) - 1, -1, -1):
            ring = polygon[x][:]
            output.append(ring)
    return output


def _orient_rings(poly):
    output = []
    polygon = poly[:]
    outer_ring = _close_ring(polygon.pop(0)[:])
    if len(outer_ring) >= 4:
        if not _ring_is_clockwise(outer_ring):
            outer_ring.reverse()
        output.append(outer_ring)
        for i in range(len(polygon)):
            hole = _close_ring(polygon[i][:])
            if len(hole) >= 4:
                if _ring_is_clockwise(hole):
                    hole.reverse()
                output.append(hole)
    return output


def _ring_is_clockwise(ring_to_test):
    total = 0
    pt1 = ring_to_test[0]
    for i in range(len(ring_to_test) - 1):
        pt2 = ring_to_test[i + 1]
        total += (pt2[0] - pt1[0]) * (pt2[1] + pt1[1])
        pt1 = pt2
    return total >= 0


def _close_ring(coordinates):
    if not _points_equal(coordinates[0], coordinates[-1]):
        coordinates.append(coordinates[0])
    return coordinates


def _points_equal(a, b):
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True
