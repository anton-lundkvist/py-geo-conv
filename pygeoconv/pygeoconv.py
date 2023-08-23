import pygeoconv._wkt as _wkt_converter
import pygeoconv._geojson as _geojson_converter
import pygeoconv._esri_json as _esri_converter


def wkt_to_esri_json(wkt: str, wkid: int = 4326):
    """
    Convert WKT to Esri Json format and set the spatial reference to the value of wkid
    wkt: str
    wkid: int
    returns a dict
    """
    if not wkt:
        raise TypeError("Unable to convert value None")
    geojson = _wkt_converter.wkt_to_geojson(wkt)
    arcgis = _geojson_converter.geojson_to_arcgis(geojson=geojson, wkid=wkid)
    return arcgis


def wkt_to_geojson(wkt_str: str):
    """
    Convert WKT to GeoJson format.
    wkt: str
    returns a dict
    """
    if not wkt_str:
        raise TypeError("Unable to convert value None")
    return _wkt_converter.wkt_to_geojson(wkt_str)


def esri_json_to_wkt(esri_json: dict):
    """
    Convert an Esri Json object to WKT format
    esri_json: dict
    returns a string
    """
    if not esri_json:
        raise TypeError("Unable to convert value None")
    geojson = _esri_converter.esri_json_to_geojson(esri_json)
    wkt = _wkt_converter.geojson_to_wkt(geojson)
    return wkt


def esri_json_to_geojson(esri_json: dict, id_attr=None):
    """
    Converts an Esri Json object to GeoJson format. If the input is an Esri Json of type feature with attributes,
    use the optional id_attr parameter to specify which attribute should be used as id of the output GeoJson feature.
    If not specified, the conversion expects an attribute with the name FID or OBJECTID to use as id, otherwise the
    conversion will fail for geometries of type Feature.
    esri_json: dict
    id_attr: Optional str
    returns a dict
    """
    if not esri_json:
        raise TypeError("Unable to convert value None")
    return _esri_converter.esri_json_to_geojson(esri_json, id_attribute=id_attr)


def geojson_to_wkt(geojson: dict):
    """
    Converts a GeoJson object to a WKT string. This conversion does not support Feature or FeatureCollection conversion.
    geojson: dict
    returns a string
    """
    if not geojson:
        raise TypeError("Unable to convert value None")
    return _wkt_converter.geojson_to_wkt(geojson)


def geojson_to_esri_json(geojson: dict, wkid: int = 4326, id_attr: str = 'OBJECTID'):
    """
    Converts a GeoJson object to Esri Json and set the spatial reference to the value of wkid.
    When converting GeoJson Feature, the id of the feature will be used as the OBJECTID of the Esri Json Feature,
    unless another field name is specified with the id_attribute
    parameter.
    geojson: dict
    wkid: int
    id_attr: Optional str
    """
    if not geojson:
        raise TypeError("Unable to convert value None")
    return _geojson_converter.geojson_to_arcgis(geojson=geojson, id_attr=id_attr, wkid=wkid)
