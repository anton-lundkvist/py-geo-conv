import pygeoconv.wkt as wkt_converter
import pygeoconv.geojson as geojson_converter
import pygeoconv.esri_json as esri_converter


def wkt_to_esri_json(wkt: str, wkid: int):
    geojson = wkt_converter.wkt_to_geojson(wkt)
    arcgis = geojson_converter.geojson_to_arcgis(geojson=geojson, wkid=wkid)
    return arcgis


def wkt_to_geojson(wkt_str: str):
    return wkt_converter.wkt_to_geojson(wkt_str)


def esri_json_to_wkt(esri_json: dict):
    geojson = esri_converter.esri_json_to_geojson(esri_json)
    wkt = wkt_converter.geojson_to_wkt(geojson)
    return wkt


def esri_json_to_geojson(esri_json: dict, id_attr=None):
    return esri_converter.esri_json_to_geojson(esri_json, id_attribute=id_attr)


def geojson_to_wkt(geojson: dict):
    return wkt_converter.geojson_to_wkt(geojson)


def geojson_to_esri_json(geojson: dict, wkid: int, id_attribute='OBJECTID'):
    return geojson_converter.geojson_to_arcgis(geojson=geojson, id_attribute=id_attribute, wkid=wkid)
