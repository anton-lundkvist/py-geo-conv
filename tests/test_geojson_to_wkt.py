import json
from pathlib import Path
import unittest

import pygeoconv


class TestGeojsonToWkt(unittest.TestCase):

    def setUp(self) -> None:
        p = Path(__file__).parent / "data" / "geojson-to-wkt.json"
        with open(p) as f:
            self.testdata = json.loads(f.read())
            self.log = False

    def test_point_geojson_to_wkt(self):
        _type = "point"
        _from = "geojson"
        _to = "wkt"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.geojson_to_wkt(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertEqual(truth, converted,
                         f"Failure: {_type} {_from} -> {_to}")

    def test_pointZ_geojson_to_wkt(self):
        _type = "pointZ"
        _from = "geojson"
        _to = "wkt"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.geojson_to_wkt(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertEqual(truth, converted,
                         f"Failure: {_type} {_from} -> {_to}")

    def test_pointMNonStandard_geojson_to_wkt(self):
        _type = "pointMNonStandard"
        _from = "geojson"
        _to = "wkt"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.geojson_to_wkt(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertEqual(truth, converted,
                         f"Failure: {_type} {_from} -> {_to}")

    def test_pointZM_geojson_to_wkt(self):
        _type = "pointZM"
        _from = "geojson"
        _to = "wkt"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.geojson_to_wkt(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertEqual(truth, converted,
                         f"Failure: {_type} {_from} -> {_to}")

    def test_pointEmpty_geojson_to_wkt(self):
        _type = "pointEmpty"
        _from = "geojson"
        _to = "wkt"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.geojson_to_wkt(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertEqual(truth, converted,
                         f"Failure: {_type} {_from} -> {_to}")

    def test_polygon_geojson_to_wkt(self):
        _type = "polygon"
        _from = "geojson"
        _to = "wkt"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.geojson_to_wkt(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertEqual(truth, converted,
                         f"Failure: {_type} {_from} -> {_to}")

    def test_polygonZ_geojson_to_wkt(self):
        _type = "polygonZ"
        _from = "geojson"
        _to = "wkt"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.geojson_to_wkt(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertEqual(truth, converted,
                         f"Failure: {_type} {_from} -> {_to}")

    def test_polygonZM_geojson_to_wkt(self):
        _type = "polygonZM"
        _from = "geojson"
        _to = "wkt"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.geojson_to_wkt(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertEqual(truth, converted,
                         f"Failure: {_type} {_from} -> {_to}")

    def test_polygonMNonStandard_geojson_to_wkt(self):
        _type = "polygonMNonStandard"
        _from = "geojson"
        _to = "wkt"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.geojson_to_wkt(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertEqual(truth, converted,
                         f"Failure: {_type} {_from} -> {_to}")

    def test_polygonEmpty_geojson_to_wkt(self):
        _type = "polygonEmpty"
        _from = "geojson"
        _to = "wkt"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.geojson_to_wkt(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertEqual(truth, converted,
                         f"Failure: {_type} {_from} -> {_to}")

    def test_multipoint_geojson_to_wkt(self):
        _type = "multipoint"
        _from = "geojson"
        _to = "wkt"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.geojson_to_wkt(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertEqual(truth, converted,
                         f"Failure: {_type} {_from} -> {_to}")

    def test_multipointZ_geojson_to_wkt(self):
        _type = "multipointZ"
        _from = "geojson"
        _to = "wkt"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.geojson_to_wkt(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertEqual(truth, converted,
                         f"Failure: {_type} {_from} -> {_to}")

    def test_multipointZM_geojson_to_wkt(self):
        _type = "multipointZM"
        _from = "geojson"
        _to = "wkt"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.geojson_to_wkt(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertEqual(truth, converted,
                         f"Failure: {_type} {_from} -> {_to}")

    def test_multipointMNonStandard_geojson_to_wkt(self):
        _type = "multipointMNonStandard"
        _from = "geojson"
        _to = "wkt"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.geojson_to_wkt(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertEqual(truth, converted,
                         f"Failure: {_type} {_from} -> {_to}")

    def test_multipointEmpty_geojson_to_wkt(self):
        _type = "multipointEmpty"
        _from = "geojson"
        _to = "wkt"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.geojson_to_wkt(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertEqual(truth, converted,
                         f"Failure: {_type} {_from} -> {_to}")

    def test_linestringZ_geojson_to_wkt(self):
        _type = "linestringZ"
        _from = "geojson"
        _to = "wkt"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.geojson_to_wkt(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertEqual(truth, converted,
                         f"Failure: {_type} {_from} -> {_to}")

    def test_linestringZM_geojson_to_wkt(self):
        _type = "linestringZM"
        _from = "geojson"
        _to = "wkt"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.geojson_to_wkt(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertEqual(truth, converted,
                         f"Failure: {_type} {_from} -> {_to}")

    def test_linestringMNonStandard_geojson_to_wkt(self):
        _type = "linestringMNonStandard"
        _from = "geojson"
        _to = "wkt"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.geojson_to_wkt(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertEqual(truth, converted,
                         f"Failure: {_type} {_from} -> {_to}")

    def test_linestringEmpty_geojson_to_wkt(self):
        _type = "linestringEmpty"
        _from = "geojson"
        _to = "wkt"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.geojson_to_wkt(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertEqual(truth, converted,
                         f"Failure: {_type} {_from} -> {_to}")

    def test_linestring_geojson_to_wkt(self):
        _type = "linestring"
        _from = "geojson"
        _to = "wkt"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.geojson_to_wkt(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertEqual(truth, converted,
                         f"Failure: {_type} {_from} -> {_to}")

    def test_multilinestring_geojson_to_wkt(self):
        _type = "multilinestring"
        _from = "geojson"
        _to = "wkt"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.geojson_to_wkt(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertEqual(truth, converted,
                         f"Failure: {_type} {_from} -> {_to}")

    def test_multilinestringZ_geojson_to_wkt(self):
        _type = "multilinestringZ"
        _from = "geojson"
        _to = "wkt"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.geojson_to_wkt(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertEqual(truth, converted,
                         f"Failure: {_type} {_from} -> {_to}")

    def test_multilinestringZM_geojson_to_wkt(self):
        _type = "multilinestringZM"
        _from = "geojson"
        _to = "wkt"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.geojson_to_wkt(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertEqual(truth, converted,
                         f"Failure: {_type} {_from} -> {_to}")

    def test_multilinestringMNonStandard_geojson_to_wkt(self):
        _type = "multilinestringMNonStandard"
        _from = "geojson"
        _to = "wkt"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.geojson_to_wkt(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertEqual(truth, converted,
                         f"Failure: {_type} {_from} -> {_to}")

    def test_multilinestringEmpty_geojson_to_wkt(self):
        _type = "multilinestringEmpty"
        _from = "geojson"
        _to = "wkt"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.geojson_to_wkt(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertEqual(truth, converted,
                         f"Failure: {_type} {_from} -> {_to}")

    def test_multipolygon_geojson_to_wkt(self):
        _type = "multipolygon"
        _from = "geojson"
        _to = "wkt"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.geojson_to_wkt(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertEqual(truth, converted,
                         f"Failure: {_type} {_from} -> {_to}")

    def test_multipolygonZ_geojson_to_wkt(self):
        _type = "multipolygonZ"
        _from = "geojson"
        _to = "wkt"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.geojson_to_wkt(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertEqual(truth, converted,
                         f"Failure: {_type} {_from} -> {_to}")

    def test_multipolygonZM_geojson_to_wkt(self):
        _type = "multipolygonZM"
        _from = "geojson"
        _to = "wkt"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.geojson_to_wkt(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertEqual(truth, converted,
                         f"Failure: {_type} {_from} -> {_to}")

    def test_multipolygonMNonStandard_geojson_to_wkt(self):
        _type = "multipolygonMNonStandard"
        _from = "geojson"
        _to = "wkt"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.geojson_to_wkt(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertEqual(truth, converted,
                         f"Failure: {_type} {_from} -> {_to}")

    def test_multipolygonEmpty_geojson_to_wkt(self):
        _type = "multipolygonEmpty"
        _from = "geojson"
        _to = "wkt"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.geojson_to_wkt(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertEqual(truth, converted,
                         f"Failure: {_type} {_from} -> {_to}")

    def test_geometrycollection_geojson_to_wkt(self):
        _type = "geometrycollection"
        _from = "geojson"
        _to = "wkt"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        converted = pygeoconv.geojson_to_wkt(source)
        if self.log:
            print(truth)
            print(converted)
        self.assertEqual(truth, converted,
                         f"Failure: {_type} {_from} -> {_to}")

    def test_unknownType_geojson_to_wkt(self):
        _type = "unknownType"
        _from = "geojson"
        _to = "wkt"
        case = self.testdata[_type]
        source = case[_from]
        truth = case[_to]
        with self.assertRaises(ValueError) as cm:
            pygeoconv.geojson_to_wkt(source)

        self.assertEqual(str(cm.exception), truth, f"Failure: {_type} {_from} -> {_to}")
