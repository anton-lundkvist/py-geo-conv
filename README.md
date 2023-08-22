# Pygeoconv

Convert between [ArcGis Json](https://developers.arcgis.com/documentation/common-data-types/geometry-objects.htm) , [WKT](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) and [GeoJson](https://geojson.org/) using python.

This tool is heavily inspired by the [terraformer-js](https://github.com/terraformer-js/terraformer) library. See more in the [Aknowledgments section](#aknowledgments).

## Requirements
pygeoconv is a pure Python implementation without dependencies, it only requires python 3.6 or greater to run. 

## Installation
```
pip install pygeoconv
```

## Usage
```
import pygeoconv

wkt_geom = "POINT (30 10)"

# Convert WKT to geojson
geojson_geom = pygeoconv.wkt_to_geojson(wkt_geom)

# Convert WKT to esri json
esri_geom = pygeoconv.wkt_to_esri_json(wkt_geom)
```


## Examples



### WKT -> GeoJson
```
import pygeoconv

wkt = """LINESTRING (495802.21253339015 6677525.294995224, 495161.84831775713 6676871.354153112, 494951.41060731944 6677661.061260023, 495261.41024527606 6677726.681621342, 495227.4686790764 6677826.243548861, 495492.2128954336 6677760.623187543, 495480.89904003375 6677869.236199382, 495657.3951842718 6677871.498970462, 495725.2783166711 6677787.776440503, 496005.861930588 6677905.440536661, 495535.2055459531 6677525.294995226, 495186.73879963695 6677532.083308466, 495225.2059079965 6677274.127405348, 495424.32976303436 6677342.010537747, 495702.6506058713 6677532.083308466, 495942.5043403487 6677663.324031104, 495994.5480751881 6677473.251260386, 495919.87662954896 6677271.864634268, 495652.8696421119 6677133.83559839, 495487.6873532736 6676946.025598751, 495517.10337731335 6676810.259333953, 495605.3514494324 6676710.697406434, 495856.51903930964 6676832.887044753, 495996.8108462681 6677052.375839511, 496026.2268703078 6677222.083670509, 496119.00048458675 6677403.105356907, 496139.36542430654 6677593.178127625, 496066.95674974733 6677726.681621343, 496023.9640992278 6677760.623187543)"""

geojson = pygeoconv.wkt_to_geojson(wkt)
```
### WKT -> Esri Json

Esri Json format (unlike WKT and GeoJson) requires the spatial reference to be specified on the geometry object. Use the wkid parameter to define which spatial reference system should be used, default is 4326.

```
esri_json = pygeoconv.wkt_to_esri_json(wkt, wkid=3006)
```

### GeoJson -> WKT
```
import pygeoconv

geojson = {
      "type": "Point",
      "coordinates": [
        495357.5879157982,
        6677582.037713626
      ]
    }

wkt = pygeoconv.geojson_to_wkt(geojson)
```

### GeoJSON -> Esri JSON
Esri Json format (unlike WKT and GeoJson) requires the spatial reference to be specified on the geometry object. Use the wkid parameter to define which spatial reference system should be used, default is EPSG:4326.
```
import pygeoconv

geojson = {
      "type": "Point",
      "coordinates": [
        495357.5879157982,
        6677582.037713626
      ]
    }
esri_json = pygeoconv.geojson_to_esri_json(geojson, wkid=3006)
```

### Esri Json -> WKT
```
import pygeoconv

esri_json = {
      "x": 495357.5879157982,
      "y": 6677582.037713626,
      "spatialReference": {
        "wkid": 3006
      }
    }

wkt = converter.esri_json_to_wkt(esri_json)
```

### Esri JSON -> GeoJSON
```
import pygeoconv

esri_json = {
      "x": 495357.5879157982,
      "y": 6677582.037713626,
      "spatialReference": {
        "wkid": 3006
      }
    }
esri_json = converter.esrijson_to_geojson(esri_json)
```

## Spatial reference system
### Esri Json
When converting to Esri Json format, use the wkid parameter to specify which spatial reference system  should be embedded in the json object. The wkid parameter expects a Well Known Id ([WKID, EPSG Code](https://spatialreference.org/)) as an integer. The default value is 4326

```
esri_json = pygeoconv.wkt_to_esri_json(wkt, wkid=3006)
```

Neither WKT or GeoJson supports defining a spatial reference system at geometry object level.

# Conversion matrices
### WKT to GeoJson or Esri Json
|               	| Point 	| LineString 	| Polygon 	| MultiPoint 	| MultiLinestring 	| MultiPolygon 	| GeometryCollection 	|
|---------------	|-------	|------------	|---------	|------------	|-----------------	|--------------	|--------------------	|
| **GeoJson**   	| Point 	| LineString 	| Polygon 	| MultiPoint 	| MultiLinestring 	| MultiPolygon 	| GeometryCollection 	|
| **Esri Json** 	| Point 	| Polyline   	| Polygon 	| MultiPoint 	| Polyline        	| Polygon      	| List of geometries 	|

### GeoJson to WKT or Esri Json
|               	| Point 	| LineString 	| Polygon 	| MultiPoint 	| MultiLinestring 	| MultiPolygon 	| GeometryCollection 	| Feature 	| FeatureCollection 	|
|---------------	|-------	|------------	|---------	|------------	|-----------------	|--------------	|--------------------	|---------	|-------------------	|
| **WKT**       	| Point 	| LineString 	| Polygon 	| MultiPoint 	| MultiLinestring 	| MultiPolygon 	| GeometryCollection 	| **      	| **                	|
| **Esri Json** 	| Point 	| Polyline   	| Polygon 	| MultiPoint 	| Polyline        	| Polygon      	| List of geometries 	| Feature 	| FeatureSet        	|

** Conversion of GeoJson Feature or FeatureCollection to WKT will throw a ValueError since WKT format has no definition for these object types.

### Esri Json to WKT or GeoJson
|             	| Point 	| Polyline                     	| Polygon                	| MultiPoint 	| Feature 	| FeatureSet        	| Envelope |
|-------------	|-------	|------------------------------	|------------------------	|------------	|---------	|-------------------	|------- |
| **WKT**     	| Point 	| LineString / MultiLineString * 	| Polygon / MultiPolygon * 	| MultiPoint 	| **      	| **                	| Polygon
| **GeoJson** 	| Point 	| LineString / MultiLineString * 	| Polygon / MultiPolygon * 	| MultiPoint 	| Feature 	| FeatureCollection 	| Polygon

\* In Esri standard, MultiLineString is described as Polyline with additional number of paths. MultiPolygon is described as Polygon with additional number of rings. For more information, see https://developers.arcgis.com/documentation/common-data-types/geometry-objects.htm

** Conversion of Esri Json Feature or FeatureSet to WKT will throw a ValueError since WKT format has no definition for these object types.

# Aknowledgments
This tool is heavily inspired by [terraformer-js](https://github.com/terraformer-js/terraformer), "A geographic toolkit for dealing with geometry, geography, formats, and building geodatabases" written in javascript.

[PLY](https://github.com/dabeaz/ply) is used for parsing WKT text based format into python dictionaries. Thanks for this awesome Python package David Beazley!

