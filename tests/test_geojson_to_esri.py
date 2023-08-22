import json
import unittest
import pygeoconv
from pygeoconv import errors


class TestGeojsonToEsri(unittest.TestCase):
    def test_point(self):
        inp = {
            "type": 'Point',
            "coordinates": [-58.7109375, 47.4609375]
        }

        output = pygeoconv.geojson_to_esri_json(inp, wkid=4326)

        self.assertEqual(output, {
            "x": -58.7109375,
            "y": 47.4609375,
            "spatialReference": {
                "wkid": 4326
            }
        })

    def test_point_z(self):
        inp = {
            "type": 'Point',
            "coordinates": [-58.7109375, 47.4609375, 10]
        }

        output = pygeoconv.geojson_to_esri_json(inp, wkid=4326)

        self.assertEqual(output, {
            "x": -58.7109375,
            "y": 47.4609375,
            "z": 10,
            "spatialReference": {
                "wkid": 4326
            }
        })

    def test_point_z_0(self):
        inp = {
            "type": 'Point',
            "coordinates": [-58.7109375, 47.4609375, 0]
        }

        output = pygeoconv.geojson_to_esri_json(inp, wkid=4326)

        self.assertEqual(output, {
            "x": -58.7109375,
            "y": 47.4609375,
            "z": 0,
            "spatialReference": {
                "wkid": 4326
            }
        })

    def test_null_point(self):
        inp = {
            "type": 'Point',
            "coordinates": [0, 0]
        }

        output = pygeoconv.geojson_to_esri_json(inp, wkid=4326)

        self.assertEqual(output, {
            "x": 0,
            "y": 0,
            "spatialReference": {
                "wkid": 4326
            }
        })

    def test_linestring(self):
        inp = {
            "type": 'LineString',
            "coordinates": [
                [21.4453125, -14.0625],
                [33.3984375, -20.7421875],
                [38.3203125, -24.609375]
            ]
        }

        output = pygeoconv.geojson_to_esri_json(inp, wkid=4326)

        self.assertEqual(output, {
            "paths": [
                [
                    [21.4453125, -14.0625],
                    [33.3984375, -20.7421875],
                    [38.3203125, -24.609375]
                ]
            ],
            "spatialReference": {
                "wkid": 4326
            }
        })

    def test_linestring_z(self):
        inp = {
            "type": 'LineString',
            "coordinates": [
                [21.4453125, -14.0625, 10],
                [33.3984375, -20.7421875, 15],
                [38.3203125, -24.609375, 12]
            ]
        }

        output = pygeoconv.geojson_to_esri_json(inp, wkid=4326)

        self.assertEqual(output, {
            "paths": [
                [
                    [21.4453125, -14.0625, 10],
                    [33.3984375, -20.7421875, 15],
                    [38.3203125, -24.609375, 12]
                ]
            ],
            "hasZ": True,
            "spatialReference": {
                "wkid": 4326
            }
        })

    def test_polygon(self):
        inp = {
            "type": 'Polygon',
            "coordinates": [
                [
                    [41.8359375, 71.015625],
                    [56.953125, 33.75],
                    [21.796875, 36.5625],
                    [41.8359375, 71.015625]
                ]
            ]
        }

        output = pygeoconv.geojson_to_esri_json(inp, wkid=4326)

        self.assertEqual(output, {
            "rings": [
                [
                    [41.8359375, 71.015625],
                    [56.953125, 33.75],
                    [21.796875, 36.5625],
                    [41.8359375, 71.015625]
                ]
            ],
            "spatialReference": {
                "wkid": 4326
            }
        })

    def test_polygon_z_values(self):
        inp = {
            "type": 'Polygon',
            "coordinates": [
                [
                    [41.8359375, 71.015625, 10],
                    [56.953125, 33.75, 15],
                    [21.796875, 36.5625, 12],
                    [41.8359375, 71.015625, 10]
                ]
            ]
        }

        output = pygeoconv.geojson_to_esri_json(inp, wkid=4326)

        self.assertEqual(output, {
            "rings": [
                [
                    [41.8359375, 71.015625, 10],
                    [56.953125, 33.75, 15],
                    [21.796875, 36.5625, 12],
                    [41.8359375, 71.015625, 10]
                ]
            ],
            "hasZ": True,
            "spatialReference": {
                "wkid": 4326
            }
        })

    def test_polygon_with_hole_to_polygon_with_two_rings(self):
        inp = {
            "type": 'Polygon',
            "coordinates": [
                [
                    [100.0, 0.0],
                    [101.0, 0.0],
                    [101.0, 1.0],
                    [100.0, 1.0],
                    [100.0, 0.0]
                ],
                [
                    [100.2, 0.2],
                    [100.8, 0.2],
                    [100.8, 0.8],
                    [100.2, 0.8],
                    [100.2, 0.2]
                ]
            ]
        }

        output = pygeoconv.geojson_to_esri_json(inp, wkid=4326)

        self.assertEqual(output, {
            "rings": [
                [[100, 0], [100, 1], [101, 1], [101, 0], [100, 0]],
                [[100.2, 0.2], [100.8, 0.2], [100.8, 0.8], [100.2, 0.8], [100.2, 0.2]]
            ],
            "spatialReference": {
                "wkid": 4326
            }
        })

    def test_strip_invalid_rings(self):
        inp = {
            "type": 'Polygon',
            "coordinates": [
                [
                    [100.0, 0.0],
                    [101.0, 0.0],
                    [101.0, 1.0],
                    [100.0, 1.0],
                    [100.0, 0.0]
                ],
                [
                    [100.2, 0.2],
                    [100.8, 0.2],
                    [100.2, 0.2]
                ]
            ]
        }

        output = pygeoconv.geojson_to_esri_json(inp, wkid=4326)

        self.assertEqual(output, {
            "rings": [
                [[100, 0], [100, 1], [101, 1], [101, 0], [100, 0]]
            ],
            "spatialReference": {
                "wkid": 4326
            }
        })

    def test_closing_polygon_rings(self):
        inp = {
            "type": 'Polygon',
            "coordinates": [
                [
                    [100.0, 0.0],
                    [101.0, 0.0],
                    [101.0, 1.0],
                    [100.0, 1.0]
                ],
                [
                    [100.2, 0.2],
                    [100.8, 0.2],
                    [100.8, 0.8],
                    [100.2, 0.8]
                ]
            ]
        }

        output = pygeoconv.geojson_to_esri_json(inp, wkid=4326)

        self.assertEqual(output, {
            "rings": [
                [[100, 0], [100, 1], [101, 1], [101, 0], [100, 0]],
                [[100.2, 0.2], [100.8, 0.2], [100.8, 0.8], [100.2, 0.8], [100.2, 0.2]]
            ],
            "spatialReference": {
                "wkid": 4326
            }
        })

    def test_multipoint(self):
        inp = {
            "type": 'MultiPoint',
            "coordinates": [
                [41.8359375, 71.015625],
                [56.953125, 33.75],
                [21.796875, 36.5625]
            ]
        }

        output = pygeoconv.geojson_to_esri_json(inp, wkid=4326)

        self.assertEqual(output, {
            "points": [
                [41.8359375, 71.015625],
                [56.953125, 33.75],
                [21.796875, 36.5625]
            ],
            "spatialReference": {
                "wkid": 4326
            }
        })

    def test_multipoint_z_values(self):
        inp = {
            "type": 'MultiPoint',
            "coordinates": [
                [41.8359375, 71.015625, 10],
                [56.953125, 33.75, 15],
                [21.796875, 36.5625, 12]
            ]
        }

        output = pygeoconv.geojson_to_esri_json(inp, wkid=4326)

        self.assertEqual(output, {
            "points": [
                [41.8359375, 71.015625, 10],
                [56.953125, 33.75, 15],
                [21.796875, 36.5625, 12]
            ],
            "hasZ": True,
            "spatialReference": {
                "wkid": 4326
            }
        })

    def test_multilinestring(self):
        inp = {
            "type": 'MultiLineString',
            "coordinates": [
                [
                    [41.8359375, 71.015625],
                    [56.953125, 33.75]
                ],
                [
                    [21.796875, 36.5625],
                    [47.8359375, 71.015625]
                ]
            ]
        }

        output = pygeoconv.geojson_to_esri_json(inp, wkid=4326)

        self.assertEqual(output, {
            "paths": [
                [
                    [41.8359375, 71.015625],
                    [56.953125, 33.75]
                ],
                [
                    [21.796875, 36.5625],
                    [47.8359375, 71.015625]
                ]
            ],
            "spatialReference": {
                "wkid": 4326
            }
        })

    def test_multilinestring_z_values(self):
        inp = {
            "type": 'MultiLineString',
            "coordinates": [
                [
                    [41.8359375, 71.015625, 10],
                    [56.953125, 33.75, 15]
                ],
                [
                    [21.796875, 36.5625, 12],
                    [47.8359375, 71.015625, 10]
                ]
            ]
        }

        output = pygeoconv.geojson_to_esri_json(inp, wkid=4326)

        self.assertEqual(output, {
            "paths": [
                [
                    [41.8359375, 71.015625, 10],
                    [56.953125, 33.75, 15]
                ],
                [
                    [21.796875, 36.5625, 12],
                    [47.8359375, 71.015625, 10]
                ]
            ],
            "hasZ": True,
            "spatialReference": {
                "wkid": 4326
            }
        })

    def test_multipolygon_to_arcgis_polygon(self):
        inp = {
            "type": 'MultiPolygon',
            "coordinates": [
                [
                    [[102.0, 2.0], [103.0, 2.0], [103.0, 3.0], [102.0, 3.0], [102.0, 2.0]]
                ],
                [
                    [[100.0, 0.0], [101.0, 0.0], [101.0, 1.0], [100.0, 1.0], [100.0, 0.0]]
                ]
            ]
        }

        output = pygeoconv.geojson_to_esri_json(inp, wkid=4326)

        self.assertEqual(output, {
            "rings": [
                [[102, 2], [102, 3], [103, 3], [103, 2], [102, 2]],
                [[100, 0], [100, 1], [101, 1], [101, 0], [100, 0]]
            ],
            "spatialReference": {
                "wkid": 4326
            }
        })

    def test_multipolygon_z_values(self):
        inp = {
            "type": 'MultiPolygon',
            "coordinates": [
                [
                    [[102.0, 2.0, 10], [103.0, 2.0, 10], [103.0, 3.0, 10], [102.0, 3.0, 10], [102.0, 2.0, 10]]
                ],
                [
                    [[100.0, 0.0, 15], [101.0, 0.0, 15], [101.0, 1.0, 15], [100.0, 1.0, 15], [100.0, 0.0, 15]]
                ]
            ]
        }

        output = pygeoconv.geojson_to_esri_json(inp, wkid=4326)

        self.assertEqual(output, {
            "rings": [
                [[102, 2, 10], [102, 3, 10], [103, 3, 10], [103, 2, 10], [102, 2, 10]],
                [[100, 0, 15], [100, 1, 15], [101, 1, 15], [101, 0, 15], [100, 0, 15]]
            ],
            "hasZ": True,
            "spatialReference": {
                "wkid": 4326
            }
        })

    def test_multipolygon_with_holes(self):
        inp = {
            "type": 'MultiPolygon',
            "coordinates": [
                [
                    [[102.0, 2.0], [103.0, 2.0], [103.0, 3.0], [102.0, 3.0], [102.0, 2.0]]
                ],
                [
                    [[100.0, 0.0], [101.0, 0.0], [101.0, 1.0], [100.0, 1.0], [100.0, 0.0]],
                    [[100.2, 0.2], [100.8, 0.2], [100.8, 0.8], [100.2, 0.8], [100.2, 0.2]]
                ]
            ]
        }

        output = pygeoconv.geojson_to_esri_json(inp, wkid=4326)
        self.assertEqual(output, {
            "spatialReference": {
                "wkid": 4326
            },
            "rings": [
                [
                    [102, 2],
                    [102, 3],
                    [103, 3],
                    [103, 2],
                    [102, 2]
                ],
                [
                    [100.2, 0.2],
                    [100.8, 0.2],
                    [100.8, 0.8],
                    [100.2, 0.8],
                    [100.2, 0.2]],
                [
                    [100, 0],
                    [100, 1],
                    [101, 1],
                    [101, 0],
                    [100, 0]
                ]
            ]
        })

    def test_closing_multipolygon_rings_with_holes(self):
        inp = {
            "type": 'MultiPolygon',
            "coordinates": [
                [
                    [[102.0, 2.0], [103.0, 2.0], [103.0, 3.0], [102.0, 3.0]]
                ],
                [
                    [[100.0, 0.0], [101.0, 0.0], [101.0, 1.0], [100.0, 1.0]],
                    [[100.2, 0.2], [100.8, 0.2], [100.8, 0.8], [100.2, 0.8]]
                ]
            ]
        }

        output = pygeoconv.geojson_to_esri_json(inp, wkid=4326)
        self.assertEqual(output, {
            "spatialReference": {
                "wkid": 4326
            },
            "rings": [
                [
                    [102, 2],
                    [102, 3],
                    [103, 3],
                    [103, 2],
                    [102, 2]
                ],
                [
                    [100.2, 0.2],
                    [100.8, 0.2],
                    [100.8, 0.8],
                    [100.2, 0.8],
                    [100.2, 0.2]
                ],
                [
                    [100, 0],
                    [100, 1],
                    [101, 1],
                    [101, 0],
                    [100, 0]
                ]
            ]
        })

    def test_feature(self):
        inp = {
            "type": 'Feature',
            "id": 'foo',
            "geometry": {
                "type": 'Polygon',
                "coordinates": [
                    [
                        [41.8359375, 71.015625],
                        [56.953125, 33.75],
                        [21.796875, 36.5625],
                        [41.8359375, 71.015625]
                    ]
                ]
            },
            "properties": {
                "foo": 'bar'
            }
        }

        output = pygeoconv.geojson_to_esri_json(inp, wkid=4326)

        self.assertEqual(output, {
            "geometry": {
                "rings": [
                    [
                        [41.8359375, 71.015625],
                        [56.953125, 33.75],
                        [21.796875, 36.5625],
                        [41.8359375, 71.015625]
                    ]
                ],
                "spatialReference": {
                    "wkid": 4326
                }
            },
            "attributes": {
                "foo": 'bar',
                "OBJECTID": 'foo'
            }
        })

    def test_feature_with_custom_id(self):
        inp = {
            "type": 'Feature',
            "id": 'foo',
            "geometry": {
                "type": 'Polygon',
                "coordinates": [
                    [[41.8359375, 71.015625],
                     [56.953125, 33.75],
                     [21.796875, 36.5625],
                     [41.8359375, 71.015625]]
                ]
            },
            "properties": {
                "foo": 'bar'
            }
        }

        output = pygeoconv.geojson_to_esri_json(inp, id_attr='myId', wkid=4326)

        self.assertEqual(output, {
            "geometry": {
                "rings": [
                    [
                        [41.8359375, 71.015625],
                        [56.953125, 33.75],
                        [21.796875, 36.5625],
                        [41.8359375, 71.015625]
                    ]
                ],
                "spatialReference": {
                    "wkid": 4326
                }
            },
            "attributes": {
                "foo": 'bar',
                "myId": 'foo'
            }
        })

    def test_feature_with_no_geometry_or_attributes(self):
        inp = {
            "type": 'Feature',
            "id": 'foo',
            "geometry": None,
            "properties": None
        }

        output = pygeoconv.geojson_to_esri_json(inp, wkid=4326)

        self.assertEqual(output, {
            "attributes": {
                "OBJECTID": 'foo'
            }
        })

    def test_feature_collection_to_array_of_features(self):
        inp = {
            "type": 'FeatureCollection',
            "features": [{
                "type": 'Feature',
                "geometry": {
                    "type": 'Point',
                    "coordinates": [102.0, 0.5]
                },
                "properties": {
                    "prop0": 'value0'
                }
            }, {
                "type": 'Feature',
                "geometry": {
                    "type": 'LineString',
                    "coordinates": [
                        [102.0, 0.0],
                        [103.0, 1.0],
                        [104.0, 0.0],
                        [105.0, 1.0]
                    ]
                },
                "properties": {
                    "prop0": 'value0'
                }
            }, {
                "type": 'Feature',
                "geometry": {
                    "type": 'Polygon',
                    "coordinates": [
                        [[100.0, 0.0],
                         [101.0, 0.0],
                         [101.0, 1.0],
                         [100.0, 1.0],
                         [100.0, 0.0]]
                    ]
                },
                "properties": {
                    "prop0": 'value0'
                }
            }]
        }

        output = pygeoconv.geojson_to_esri_json(inp, wkid=4326)

        self.assertEqual(output, [{
            "geometry": {
                "x": 102,
                "y": 0.5,
                "spatialReference": {
                    "wkid": 4326
                }
            },
            "attributes": {
                "prop0": 'value0'
            }
        }, {
            "geometry": {
                "paths": [
                    [[102, 0],
                     [103, 1],
                     [104, 0],
                     [105, 1]]
                ],
                "spatialReference": {
                    "wkid": 4326
                }
            },
            "attributes": {
                "prop0": 'value0'
            }
        }, {
            "geometry": {
                "rings": [
                    [[100, 0],
                     [100, 1],
                     [101, 1],
                     [101, 0],
                     [100, 0]]
                ],
                "spatialReference": {
                    "wkid": 4326
                }
            },
            "attributes": {
                "prop0": 'value0'
            }
        }])

    def test_geometry_collection(self):
        inp = {
            "type": 'GeometryCollection',
            "geometries": [{
                "type": 'Polygon',
                "coordinates": [[[-95, 43], [-95, 50], [-90, 50], [-91, 42], [-95, 43]]]
            }, {
                "type": 'LineString',
                "coordinates": [[-89, 42], [-89, 50], [-80, 50], [-80, 42]]
            }, {
                "type": 'Point',
                "coordinates": [-94, 46]
            }]
        }

        output = pygeoconv.geojson_to_esri_json(inp, wkid=4326)

        self.assertEqual(output, [{
            "rings": [
                [[-95, 43],
                 [-95, 50],
                 [-90, 50],
                 [-91, 42],
                 [-95, 43]]
            ],
            "spatialReference": {
                "wkid": 4326
            }
        }, {
            "paths": [
                [[-89, 42],
                 [-89, 50],
                 [-80, 50],
                 [-80, 42]]
            ],
            "spatialReference": {
                "wkid": 4326
            }
        }, {
            "x": -94,
            "y": 46,
            "spatialReference": {
                "wkid": 4326
            }
        }])

    def test_unknown_geometry_type(self):
        geojson = {
            "type": "unknown", "geometry": {}
        }
        with self.assertRaises(errors.GeojsonParserError):
            pygeoconv.geojson_to_esri_json(geojson, wkid=4326)

    def test_no_type(self):
        geojson = {
            "noType": "", "geometry": {}
        }
        with self.assertRaises(errors.GeojsonParserError):
            pygeoconv.geojson_to_esri_json(geojson, wkid=4326)

    def test_no_geometry(self):
        geojson = {
            "type": "Point"
        }
        with self.assertRaises(errors.GeojsonParserError):
            pygeoconv.geojson_to_esri_json(geojson, wkid=4326)

    def test_should_not_modify_original_object(self):
        geojson = {
            "type": 'FeatureCollection',
            "features": [{
                "type": 'Feature',
                "geometry": {
                    "type": 'Point',
                    "coordinates": [102.0, 0.5]
                },
                "properties": {
                    "prop0": 'value0'
                }
            }, {
                "type": 'Feature',
                "geometry": {
                    "type": 'LineString',
                    "coordinates": [
                        [102.0, 0.0],
                        [103.0, 1.0],
                        [104.0, 0.0],
                        [105.0, 1.0]
                    ]
                },
                "properties": {
                    "prop0": 'value0'
                }
            }, {
                "type": 'Feature',
                "geometry": {
                    "type": 'Polygon',
                    "coordinates": [
                        [[100.0, 0.0],
                         [101.0, 0.0],
                         [101.0, 1.0],
                         [100.0, 1.0],
                         [100.0, 0.0]]
                    ]
                },
                "properties": {
                    "prop0": 'value0'
                }
            }]
        }

        original = json.dumps(geojson)

        pygeoconv.geojson_to_esri_json(geojson, wkid=4326)

        self.assertEqual(original, json.dumps(geojson))
