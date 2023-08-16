# Py-geo-conv

Convert between ArcGis Json(https://developers.arcgis.com/documentation/common-data-types/geometry-objects.htm) , WKT(https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) and GeoJson(https://geojson.org/)

## Usage
Kod för konvertering finns i mappen `geometry_conversion` och importeras genom
```
import geometry_conversion.geom_converter as converter
```
Koden har inga beroenden mer än standardinstallation av python 3.x


## Exempel



### Exempel på konvertering från WKT till GeoJSON och Esri JSON
```
import geometry_conversion.geom_converter as converter

wkt = """LINESTRING (495802.21253339015 6677525.294995224, 495161.84831775713 6676871.354153112, 494951.41060731944 6677661.061260023, 495261.41024527606 6677726.681621342, 495227.4686790764 6677826.243548861, 495492.2128954336 6677760.623187543, 495480.89904003375 6677869.236199382, 495657.3951842718 6677871.498970462, 495725.2783166711 6677787.776440503, 496005.861930588 6677905.440536661, 495535.2055459531 6677525.294995226, 495186.73879963695 6677532.083308466, 495225.2059079965 6677274.127405348, 495424.32976303436 6677342.010537747, 495702.6506058713 6677532.083308466, 495942.5043403487 6677663.324031104, 495994.5480751881 6677473.251260386, 495919.87662954896 6677271.864634268, 495652.8696421119 6677133.83559839, 495487.6873532736 6676946.025598751, 495517.10337731335 6676810.259333953, 495605.3514494324 6676710.697406434, 495856.51903930964 6676832.887044753, 495996.8108462681 6677052.375839511, 496026.2268703078 6677222.083670509, 496119.00048458675 6677403.105356907, 496139.36542430654 6677593.178127625, 496066.95674974733 6677726.681621343, 496023.9640992278 6677760.623187543)"""

# WKT -> GeoJSON
geojson = converter.wkt_to_geojson(wkt)

# WKT -> Esri JSON
esri_json = converter.wkt_to_esri_json(wkt, wkid=3006)
```

### Exempel på konvertering från GeoJSON till WKT och Esri JSON
```
import geometry_conversion.geom_converter as converter

geojson = {
      "type": "Point",
      "coordinates": [
        495357.5879157982,
        6677582.037713626
      ]
    }

# GeoJSON -> WKT
wkt = converter.geojson_to_wkt(geojson)

# GeoJSON -> Esri JSON
esri_json = converter.geojson_to_esri_json(geojson, wkid=3006)
```

### Exempel på konvertering från Esri JSON till WKT och GeoJSON
```
import geometry_conversion.geom_converter as converter

esri_json = {
      "x": 495357.5879157982,
      "y": 6677582.037713626,
      "spatialReference": {
        "wkid": 3006
      }
    }

# Esri JSON -> WKT
wkt = converter.esri_json_to_wkt(esri_json)

# Esri JSON -> GeoJSON
esri_json = converter.esrijson_to_geojson(esri_json)
```

## Spatiala referenssystem
### Esri JSON
Vid konvertering till Esri JSON kan referenssystem anges med epsg-kod mha wkid parametern, vilket då sätts på Esri JSON objektet:
```
# WKT -> Esri JSON
esri_json = converter.wkt_to_esri_json(wkt, wkid=3006)
```

Varken WKT eller GeoJSON har stöd för angivelse av referenssystem på geometrinivå

## Geometrityper

Konverteringen stödjer följande geometrityper för WKT:
- Point
- Linestring
- Polygon
- Multipoint
- MultiLineString
- MultiPolygon
- GeometryCollection

Konverteringen stödjer följande geometrityper för GeoJSON:
- Point
- Linestring
- Polygon
- Multipoint
- MultiLineString
- MultiPolygon
- GeometryCollection

Konverteringen stödjer följande geometrityper för EsriJSON:
- Point
- Polyline
- Polygon
- Multipoint

Då Esri, till skillnad från WKT och GeoJSON, inte skiljer på Linestring vs MultiLineString eller Polygon vs MultiPolygon, så översätts dessa till Polyline respektive Polygon. Se https://developers.arcgis.com/documentation/common-data-types/geometry-objects.htm


## Tester
Tester finns under mappen `tests` och använder pythons unittest modul

## 