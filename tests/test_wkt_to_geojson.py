import json
import unittest
from pathlib import Path

import pygeoconv


class TestWktToGeojson(unittest.TestCase):

    def setUp(self) -> None:
        p = Path(__file__).parent/"data"/"wkt-to-geojson.json"
        with open(p) as f:
            self.testdata = json.loads(f.read())
            self.log = False

    def test_point_wkt_to_geojson(self):
        _type = "point"
        _from = "wkt"
        _to = "geojson"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.wkt_to_geojson(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertDictEqual(truth, converted,
                             f"Failure: {_type} {_from} -> {_to}")

    def test_pointEmpty_wkt_to_geojson(self):
        _type = "pointEmpty"
        _from = "wkt"
        _to = "geojson"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.wkt_to_geojson(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertDictEqual(truth, converted,
                             f"Failure: {_type} {_from} -> {_to}")

    def test_pointZ_wkt_to_geojson(self):
        _type = "pointZ"
        _from = "wkt"
        _to = "geojson"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.wkt_to_geojson(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertDictEqual(truth, converted,
                             f"Failure: {_type} {_from} -> {_to}")

    def test_pointM_wkt_to_geojson(self):
        _type = "pointM"
        _from = "wkt"
        _to = "geojson"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.wkt_to_geojson(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertDictEqual(truth, converted,
                             f"Failure: {_type} {_from} -> {_to}")

    def test_pointZM_wkt_to_geojson(self):
        _type = "pointZM"
        _from = "wkt"
        _to = "geojson"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.wkt_to_geojson(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertDictEqual(truth, converted,
                             f"Failure: {_type} {_from} -> {_to}")

    def test_pointScientificNotation_wkt_to_geojson(self):
        _type = "pointScientificNotation"
        _from = "wkt"
        _to = "geojson"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.wkt_to_geojson(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertDictEqual(truth, converted,
                             f"Failure: {_type} {_from} -> {_to}")

    def test_linestring_wkt_to_geojson(self):
        _type = "linestring"
        _from = "wkt"
        _to = "geojson"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.wkt_to_geojson(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertDictEqual(truth, converted,
                             f"Failure: {_type} {_from} -> {_to}")

    def test_linestringEmpty_wkt_to_geojson(self):
        _type = "linestringEmpty"
        _from = "wkt"
        _to = "geojson"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.wkt_to_geojson(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertDictEqual(truth, converted,
                             f"Failure: {_type} {_from} -> {_to}")

    def test_linestringZ_wkt_to_geojson(self):
        _type = "linestringZ"
        _from = "wkt"
        _to = "geojson"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.wkt_to_geojson(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertDictEqual(truth, converted,
                             f"Failure: {_type} {_from} -> {_to}")

    def test_linestringM_wkt_to_geojson(self):
        _type = "linestringM"
        _from = "wkt"
        _to = "geojson"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.wkt_to_geojson(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertDictEqual(truth, converted,
                             f"Failure: {_type} {_from} -> {_to}")

    def test_linestringZM_wkt_to_geojson(self):
        _type = "linestringZM"
        _from = "wkt"
        _to = "geojson"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.wkt_to_geojson(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertDictEqual(truth, converted,
                             f"Failure: {_type} {_from} -> {_to}")

    def test_polygon_wkt_to_geojson(self):
        _type = "polygon"
        _from = "wkt"
        _to = "geojson"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.wkt_to_geojson(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertDictEqual(truth, converted,
                             f"Failure: {_type} {_from} -> {_to}")

    def test_polygonEmpty_wkt_to_geojson(self):
        _type = "polygonEmpty"
        _from = "wkt"
        _to = "geojson"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.wkt_to_geojson(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertDictEqual(truth, converted,
                             f"Failure: {_type} {_from} -> {_to}")

    def test_polygonZ_wkt_to_geojson(self):
        _type = "polygonZ"
        _from = "wkt"
        _to = "geojson"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.wkt_to_geojson(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertDictEqual(truth, converted,
                             f"Failure: {_type} {_from} -> {_to}")

    def test_polygonM_wkt_to_geojson(self):
        _type = "polygonM"
        _from = "wkt"
        _to = "geojson"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.wkt_to_geojson(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertDictEqual(truth, converted,
                             f"Failure: {_type} {_from} -> {_to}")

    def test_polygonZM_wkt_to_geojson(self):
        _type = "polygonZM"
        _from = "wkt"
        _to = "geojson"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.wkt_to_geojson(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertDictEqual(truth, converted,
                             f"Failure: {_type} {_from} -> {_to}")

    def test_polygonWithHole_wkt_to_geojson(self):
        _type = "polygonWithHole"
        _from = "wkt"
        _to = "geojson"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.wkt_to_geojson(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertDictEqual(truth, converted,
                             f"Failure: {_type} {_from} -> {_to}")

    def test_multiPoint_wkt_to_geojson(self):
        _type = "multiPoint"
        _from = "wkt"
        _to = "geojson"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.wkt_to_geojson(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertDictEqual(truth, converted,
                             f"Failure: {_type} {_from} -> {_to}")

    def test_multiPointEmpty_wkt_to_geojson(self):
        _type = "multiPointEmpty"
        _from = "wkt"
        _to = "geojson"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.wkt_to_geojson(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertDictEqual(truth, converted,
                             f"Failure: {_type} {_from} -> {_to}")

    def test_multiPointZ_wkt_to_geojson(self):
        _type = "multiPointZ"
        _from = "wkt"
        _to = "geojson"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.wkt_to_geojson(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertDictEqual(truth, converted,
                             f"Failure: {_type} {_from} -> {_to}")

    def test_multiPointM_wkt_to_geojson(self):
        _type = "multiPointM"
        _from = "wkt"
        _to = "geojson"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.wkt_to_geojson(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertDictEqual(truth, converted,
                             f"Failure: {_type} {_from} -> {_to}")

    def test_multiPointZM_wkt_to_geojson(self):
        _type = "multiPointZM"
        _from = "wkt"
        _to = "geojson"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.wkt_to_geojson(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertDictEqual(truth, converted,
                             f"Failure: {_type} {_from} -> {_to}")

    def test_multiPointAlternateSyntax_wkt_to_geojson(self):
        _type = "multiPointAlternateSyntax"
        _from = "wkt"
        _to = "geojson"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.wkt_to_geojson(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertDictEqual(truth, converted,
                             f"Failure: {_type} {_from} -> {_to}")

    def test_multiPointAlternateSyntaxAndZ_wkt_to_geojson(self):
        _type = "multiPointAlternateSyntaxAndZ"
        _from = "wkt"
        _to = "geojson"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.wkt_to_geojson(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertDictEqual(truth, converted,
                             f"Failure: {_type} {_from} -> {_to}")

    def test_multiPointAlternateSyntaxAndM_wkt_to_geojson(self):
        _type = "multiPointAlternateSyntaxAndM"
        _from = "wkt"
        _to = "geojson"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.wkt_to_geojson(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertDictEqual(truth, converted,
                             f"Failure: {_type} {_from} -> {_to}")

    def test_multiPointAlternateSyntaxAndZM_wkt_to_geojson(self):
        _type = "multiPointAlternateSyntaxAndZM"
        _from = "wkt"
        _to = "geojson"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.wkt_to_geojson(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertDictEqual(truth, converted,
                             f"Failure: {_type} {_from} -> {_to}")

    def test_multilinestringAlternateSyntax_wkt_to_geojson(self):
        _type = "multilinestringAlternateSyntax"
        _from = "wkt"
        _to = "geojson"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.wkt_to_geojson(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertDictEqual(truth, converted,
                             f"Failure: {_type} {_from} -> {_to}")

    def test_multilinestringEmpty_wkt_to_geojson(self):
        _type = "multilinestringEmpty"
        _from = "wkt"
        _to = "geojson"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.wkt_to_geojson(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertDictEqual(truth, converted,
                             f"Failure: {_type} {_from} -> {_to}")

    def test_multilinestringAlternateSyntaxZ_wkt_to_geojson(self):
        _type = "multilinestringAlternateSyntaxZ"
        _from = "wkt"
        _to = "geojson"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.wkt_to_geojson(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertDictEqual(truth, converted,
                             f"Failure: {_type} {_from} -> {_to}")

    def test_multilinestringAlternateSyntaxM_wkt_to_geojson(self):
        _type = "multilinestringAlternateSyntaxM"
        _from = "wkt"
        _to = "geojson"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.wkt_to_geojson(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertDictEqual(truth, converted,
                             f"Failure: {_type} {_from} -> {_to}")

    def test_multilinestringAlternateSyntaxZM_wkt_to_geojson(self):
        _type = "multilinestringAlternateSyntaxZM"
        _from = "wkt"
        _to = "geojson"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.wkt_to_geojson(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertDictEqual(truth, converted,
                             f"Failure: {_type} {_from} -> {_to}")

    def test_multipolygon_wkt_to_geojson(self):
        _type = "multipolygon"
        _from = "wkt"
        _to = "geojson"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.wkt_to_geojson(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertDictEqual(truth, converted,
                             f"Failure: {_type} {_from} -> {_to}")

    def test_multipolygonEmpty_wkt_to_geojson(self):
        _type = "multipolygonEmpty"
        _from = "wkt"
        _to = "geojson"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.wkt_to_geojson(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertDictEqual(truth, converted,
                             f"Failure: {_type} {_from} -> {_to}")

    def test_multipolygonZ_wkt_to_geojson(self):
        _type = "multipolygonZ"
        _from = "wkt"
        _to = "geojson"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.wkt_to_geojson(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertDictEqual(truth, converted,
                             f"Failure: {_type} {_from} -> {_to}")

    def test_multipolygonM_wkt_to_geojson(self):
        _type = "multipolygonM"
        _from = "wkt"
        _to = "geojson"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.wkt_to_geojson(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertDictEqual(truth, converted,
                             f"Failure: {_type} {_from} -> {_to}")

    def test_multipolygonZM_wkt_to_geojson(self):
        _type = "multipolygonZM"
        _from = "wkt"
        _to = "geojson"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.wkt_to_geojson(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertDictEqual(truth, converted,
                             f"Failure: {_type} {_from} -> {_to}")

    def test_multipolygonHole_wkt_to_geojson(self):
        _type = "multipolygonHole"
        _from = "wkt"
        _to = "geojson"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.wkt_to_geojson(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertDictEqual(truth, converted,
                             f"Failure: {_type} {_from} -> {_to}")

    def test_geometryCollection_wkt_to_geojson(self):
        _type = "geometryCollection"
        _from = "wkt"
        _to = "geojson"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.wkt_to_geojson(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertDictEqual(truth, converted,
                             f"Failure: {_type} {_from} -> {_to}")

    def test_geometryCollection2_wkt_to_geojson(self):
        _type = "geometryCollection2"
        _from = "wkt"
        _to = "geojson"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.wkt_to_geojson(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertDictEqual(truth, converted,
                             f"Failure: {_type} {_from} -> {_to}")

    def test_geometryCollectionWithoutPoints_wkt_to_geojson(self):
        _type = "geometryCollectionWithoutPoints"
        _from = "wkt"
        _to = "geojson"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.wkt_to_geojson(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertDictEqual(truth, converted,
                             f"Failure: {_type} {_from} -> {_to}")

    def test_geometryCollectionWithoutLines_wkt_to_geojson(self):
        _type = "geometryCollectionWithoutLines"
        _from = "wkt"
        _to = "geojson"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.wkt_to_geojson(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertDictEqual(truth, converted,
                             f"Failure: {_type} {_from} -> {_to}")

    def test_geometryCollectionWithoutPolygons_wkt_to_geojson(self):
        _type = "geometryCollectionWithoutPolygons"
        _from = "wkt"
        _to = "geojson"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.wkt_to_geojson(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertDictEqual(truth, converted,
                             f"Failure: {_type} {_from} -> {_to}")

    def test_geometryCollectionEmpty_wkt_to_geojson(self):
        _type = "geometryCollectionEmpty"
        _from = "wkt"
        _to = "geojson"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.wkt_to_geojson(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertDictEqual(truth, converted,
                             f"Failure: {_type} {_from} -> {_to}")

    def test_geometryCollectionEmptyPoint_wkt_to_geojson(self):
        _type = "geometryCollectionEmptyPoint"
        _from = "wkt"
        _to = "geojson"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.wkt_to_geojson(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertDictEqual(truth, converted,
                             f"Failure: {_type} {_from} -> {_to}")

    def test_geometryCollectionEmptyAndNoneEmpty_wkt_to_geojson(self):
        _type = "geometryCollectionEmptyAndNoneEmpty"
        _from = "wkt"
        _to = "geojson"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.wkt_to_geojson(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertDictEqual(truth, converted,
                             f"Failure: {_type} {_from} -> {_to}")

    def test_geometryCollectionZ_wkt_to_geojson(self):
        _type = "geometryCollectionZ"
        _from = "wkt"
        _to = "geojson"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.wkt_to_geojson(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertDictEqual(truth, converted,
                             f"Failure: {_type} {_from} -> {_to}")

    def test_geometryCollectionM_wkt_to_geojson(self):
        _type = "geometryCollectionM"
        _from = "wkt"
        _to = "geojson"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.wkt_to_geojson(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertDictEqual(truth, converted,
                             f"Failure: {_type} {_from} -> {_to}")

    def test_geometryCollectionInGeometryCollection_wkt_to_geojson(self):
        _type = "geometryCollectionInGeometryCollection"
        _from = "wkt"
        _to = "geojson"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.wkt_to_geojson(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertDictEqual(truth, converted,
                             f"Failure: {_type} {_from} -> {_to}")

    def test_geometryCollectionZM_wkt_to_geojson(self):
        _type = "geometryCollectionZM"
        _from = "wkt"
        _to = "geojson"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.wkt_to_geojson(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertDictEqual(truth, converted,
                             f"Failure: {_type} {_from} -> {_to}")
