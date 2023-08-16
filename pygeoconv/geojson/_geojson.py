from pygeoconv._common import _shallow_clone, _orient_rings, _flatten_multi_polygon_rings


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
