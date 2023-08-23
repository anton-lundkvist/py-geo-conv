from pygeoconv._wkt_parser import wkt_parser
from pygeoconv.errors import WktParserError


def _array_to_ring(arr):
    parts = []
    for item in arr:
        parts.append(' '.join(str(x) for x in item))
    return '(' + ', '.join(parts) + ')'


def _point_to_wkt_point(geojson):
    ret = 'POINT '
    if 'coordinates' not in geojson or len(geojson['coordinates']) == 0:
        ret += 'EMPTY'
        return ret
    elif len(geojson['coordinates']) == 3:
        if 'properties' in geojson and geojson['properties'].get('m') == True:
            ret += 'M '
        else:
            ret += 'Z '
    elif len(geojson['coordinates']) == 4:
        ret += 'ZM '
    ret += '(' + ' '.join(str(x) for x in geojson['coordinates']) + ')'
    return ret


def _line_string_to_wkt_line_string(geojson):
    ret = 'LINESTRING '
    if 'coordinates' not in geojson or len(geojson['coordinates']) == 0 or len(geojson['coordinates'][0]) == 0:
        ret += 'EMPTY'
        return ret
    elif len(geojson['coordinates'][0]) == 3:
        if 'properties' in geojson and geojson['properties'].get('m') == True:
            ret += 'M '
        else:
            ret += 'Z '
    elif len(geojson['coordinates'][0]) == 4:
        ret += 'ZM '
    ret += _array_to_ring(geojson['coordinates'])
    return ret


def _polygon_to_wkt_polygon(geojson):
    ret = 'POLYGON '
    if 'coordinates' not in geojson or len(geojson['coordinates']) == 0 or len(geojson['coordinates'][0]) == 0:
        ret += 'EMPTY'
        return ret
    elif len(geojson['coordinates'][0][0]) == 3:
        if 'properties' in geojson and geojson['properties'].get('m') == True:
            ret += 'M '
        else:
            ret += 'Z '
    elif len(geojson['coordinates'][0][0]) == 4:
        ret += 'ZM '
    ret += '('
    parts = []
    for item in geojson['coordinates']:
        parts.append(_array_to_ring(item))
    ret += ', '.join(parts)
    ret += ')'
    return ret


def _multi_point_to_wkt_multi_point(geojson):
    ret = 'MULTIPOINT '
    if 'coordinates' not in geojson or len(geojson['coordinates']) == 0 or len(geojson['coordinates'][0]) == 0:
        ret += 'EMPTY'
        return ret
    elif len(geojson['coordinates'][0]) == 3:
        if 'properties' in geojson and geojson['properties'].get('m') == True:
            ret += 'M '
        else:
            ret += 'Z '
    elif len(geojson['coordinates'][0]) == 4:
        ret += 'ZM '
    ret += _array_to_ring(geojson['coordinates'])
    return ret


def _multi_line_string_to_wkt_multi_line_string(geojson):
    ret = 'MULTILINESTRING '
    if 'coordinates' not in geojson or len(geojson['coordinates']) == 0 or len(geojson['coordinates'][0]) == 0:
        ret += 'EMPTY'
        return ret
    elif len(geojson['coordinates'][0][0]) == 3:
        if 'properties' in geojson and geojson['properties'].get('m') == True:
            ret += 'M '
        else:
            ret += 'Z '
    elif len(geojson['coordinates'][0][0]) == 4:
        ret += 'ZM '
    ret += '('
    parts = []
    for item in geojson['coordinates']:
        parts.append(_array_to_ring(item))
    ret += ', '.join(parts)
    ret += ')'
    return ret


def _multi_polygon_to_wkt_multi_polygon(geojson):
    ret = 'MULTIPOLYGON '
    if 'coordinates' not in geojson or len(geojson['coordinates']) == 0 or len(geojson['coordinates'][0]) == 0:
        ret += 'EMPTY'
        return ret
    elif len(geojson['coordinates'][0][0][0]) == 3:
        if 'properties' in geojson and geojson['properties'].get('m') == True:
            ret += 'M '
        else:
            ret += 'Z '
    elif len(geojson['coordinates'][0][0][0]) == 4:
        ret += 'ZM '
    ret += '('
    inner = []
    for item in geojson['coordinates']:
        it = '('
        parts = []
        for subitem in item:
            parts.append(_array_to_ring(subitem))
        it += ', '.join(parts)
        it += ')'
        inner.append(it)
    ret += ', '.join(inner)
    ret += ')'
    return ret


def geojson_to_wkt(geojson):
    if geojson['type'] == 'Point':
        return _point_to_wkt_point(geojson)
    elif geojson['type'] == 'LineString':
        return _line_string_to_wkt_line_string(geojson)
    elif geojson['type'] == 'Polygon':
        return _polygon_to_wkt_polygon(geojson)
    elif geojson['type'] == 'MultiPoint':
        return _multi_point_to_wkt_multi_point(geojson)
    elif geojson['type'] == 'MultiLineString':
        return _multi_line_string_to_wkt_multi_line_string(geojson)
    elif geojson['type'] == 'MultiPolygon':
        return _multi_polygon_to_wkt_multi_polygon(geojson)
    elif geojson['type'] == 'GeometryCollection':
        ret = 'GEOMETRYCOLLECTION'
        parts = []
        for item in geojson['geometries']:
            parts.append(geojson_to_wkt(item))
        return ret + '(' + ', '.join(parts) + ')'
    else:
        raise ValueError('Unknown Type: ' + geojson['type'])


def wkt_to_geojson(wkt: str) -> dict:
    try:
        parsed = wkt_parser.parse(wkt)
        return parsed
    except Exception as e:
        raise WktParserError(f"Unable to parse WKT string: {e}")
