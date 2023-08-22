import json
import unittest
import pygeoconv
from pygeoconv.errors import EsriJsonParserError


class TestEsrijsonToGeojson(unittest.TestCase):

    def test_point_conversion(self):
        inp = {
            "x": -66.796875,
            "y": 20.0390625,
            "spatialReference": {
                "wkid": 4326
            }
        }

        output = pygeoconv.esri_json_to_geojson(inp)

        self.assertEqual(output.get("coordinates"), [-66.796875, 20.0390625])

    def test_point_z(self):
        inp = {
            "x": -66.796875,
            "y": 20.0390625,
            "z": 1,
            "spatialReference": {
                "wkid": 4326
            }
        }

        output = pygeoconv.esri_json_to_geojson(inp)

        self.assertEqual(output.get("coordinates"), [-66.796875, 20.0390625, 1])

    def tes_point_zero(self):
        inp = {
            "x": 0,
            "y": 0,
            "spatialReference": {
                "wkid": 4326
            }
        }

        output = pygeoconv.esri_json_to_geojson(inp)

        self.assertEqual(output.get("coordinates"), [0, 0])

    def test_nan_coordinates(self):
        inp = {
            "geometry": {
                "x": 'NaN',
                "y": 'NaN'
            },
            "attributes": {
                "foo": 'bar'
            }
        }
        output = pygeoconv.esri_json_to_geojson(inp)
        self.assertEqual(output.get("properties").get("foo"), 'bar')
        self.assertEqual(output.get("geometry").get("coordinates"), [])

    def test_polyline(self):
        inp = {
            "paths": [
                [[6.6796875, 47.8125],
                 [-65.390625, 52.3828125],
                 [-52.3828125, 42.5390625]]
            ],
            "spatialReference": {
                "wkid": 4326
            }
        }

        output = pygeoconv.esri_json_to_geojson(inp)

        self.assertEqual(output.get("coordinates"), [
            [6.6796875, 47.8125],
            [-65.390625, 52.3828125],
            [-52.3828125, 42.5390625]
        ])

    def test_polyline_z(self):
        inp = {
            "paths": [
                [[6.6796875, 47.8125, 1],
                 [-65.390625, 52.3828125, 1],
                 [-52.3828125, 42.5390625, 1]]
            ],
            "spatialReference": {
                "wkid": 4326
            }
        }

        output = pygeoconv.esri_json_to_geojson(inp)

        self.assertEqual(output.get("coordinates"), [
            [6.6796875, 47.8125, 1],
            [-65.390625, 52.3828125, 1],
            [-52.3828125, 42.5390625, 1]
        ])

    def test_polygon(self):
        inp = {
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
        }

        output = pygeoconv.esri_json_to_geojson(inp)

        self.assertEqual(output.get("coordinates"), [
            [
                [41.8359375, 71.015625],
                [21.796875, 36.5625],
                [56.953125, 33.75],
                [41.8359375, 71.015625]
            ]
        ])

        self.assertEqual(output.get("type"), 'Polygon')

    def test_polygon_z(self):
        inp = {
            "rings": [
                [
                    [41.8359375, 71.015625, 1],
                    [56.953125, 33.75, 1],
                    [21.796875, 36.5625, 1],
                    [41.8359375, 71.015625, 1]
                ]
            ],
            "spatialReference": {
                "wkid": 4326
            }
        }

        output = pygeoconv.esri_json_to_geojson(inp)

        self.assertEqual(output.get("coordinates"), [
            [
                [41.8359375, 71.015625, 1],
                [21.796875, 36.5625, 1],
                [56.953125, 33.75, 1],
                [41.8359375, 71.015625, 1]
            ]
        ])

        self.assertEqual(output.get("type"), 'Polygon')

    def test_unclosed_rings(self):
        inp = {
            "rings": [
                [
                    [41.8359375, 71.015625],
                    [56.953125, 33.75],
                    [21.796875, 36.5625]
                ]
            ],
            "spatialReference": {
                "wkid": 4326
            }
        }

        output = pygeoconv.esri_json_to_geojson(inp)

        self.assertEqual(output.get("coordinates"), [
            [
                [41.8359375, 71.015625],
                [21.796875, 36.5625],
                [56.953125, 33.75],
                [41.8359375, 71.015625]
            ]
        ])

        self.assertEqual(output.get("type"), 'Polygon')

    def test_multipoint(self):
        inp = {
            "points": [
                [41.8359375, 71.015625],
                [56.953125, 33.75],
                [21.796875, 36.5625]
            ],
            "spatialReference": {
                "wkid": 4326
            }
        }

        output = pygeoconv.esri_json_to_geojson(inp)

        self.assertEqual(output.get("coordinates"), [
            [41.8359375, 71.015625],
            [56.953125, 33.75],
            [21.796875, 36.5625]
        ])

    def test_polyline_2(self):
        inp = {
            "paths": [
                [
                    [41.8359375, 71.015625],
                    [56.953125, 33.75]
                ],
                [
                    [21.796875, 36.5625],
                    [41.8359375, 71.015625]
                ]
            ],
            "spatialReference": {
                "wkid": 4326
            }
        }

        output = pygeoconv.esri_json_to_geojson(inp)

        self.assertEqual(output.get("coordinates"), [
            [
                [41.8359375, 71.015625],
                [56.953125, 33.75]
            ],
            [
                [21.796875, 36.5625],
                [41.8359375, 71.015625]
            ]
        ])

    def test_polygon_to_multipolygon(self):
        inp = {
            "rings": [
                [
                    [-122.63, 45.52],
                    [-122.57, 45.53],
                    [-122.52, 45.50],
                    [-122.49, 45.48],
                    [-122.64, 45.49],
                    [-122.63, 45.52],
                    [-122.63, 45.52]
                ],
                [
                    [-83, 35],
                    [-74, 35],
                    [-74, 41],
                    [-83, 41],
                    [-83, 35]
                ]
            ],
            "spatialReference": {
                "wkid": 4326
            }
        }

        output = pygeoconv.esri_json_to_geojson(inp)
        expected = [
            [
                [
                    [-122.63, 45.52],
                    [-122.63, 45.52],
                    [-122.64, 45.49],
                    [-122.49, 45.48],
                    [-122.52, 45.5],
                    [-122.57, 45.53],
                    [-122.63, 45.52]
                ]
            ],
            [
                [
                    [-83, 35],
                    [-74, 35],
                    [-74, 41],
                    [-83, 41],
                    [-83, 35]
                ]
            ]
        ]

        self.assertEqual(output.get("coordinates"), expected)
        self.assertEqual(output.get("type"), 'MultiPolygon')

    def test_strip_invalid_rings(self):
        inp = {
            "rings": [
                [
                    [-122.63, 45.52],
                    [-122.57, 45.53],
                    [-122.52, 45.50],
                    [-122.49, 45.48],
                    [-122.64, 45.49],
                    [-122.63, 45.52],
                    [-122.63, 45.52]
                ],
                [
                    [-83, 35],
                    [-74, 35],
                    [-83, 35]
                ]
            ],
            "spatialReference": {
                "wkid": 4326
            }
        }

        output = pygeoconv.esri_json_to_geojson(inp)

        self.assertEqual(output.get("coordinates"), [
            [
                [-122.63, 45.52],
                [-122.63, 45.52],
                [-122.64, 45.49],
                [-122.49, 45.48],
                [-122.52, 45.5],
                [-122.57, 45.53],
                [-122.63, 45.52]
            ]
        ])
        self.assertEqual(output.get("type"), 'Polygon')

    def test_close_rings(self):
        inp = {
            "rings": [
                [
                    [-122.63, 45.52],
                    [-122.57, 45.53],
                    [-122.52, 45.50],
                    [-122.49, 45.48],
                    [-122.64, 45.49]
                ],
                [
                    [-83, 35],
                    [-74, 35],
                    [-74, 41],
                    [-83, 41]
                ]
            ],
            "spatialReference": {
                "wkid": 4326
            }
        }

        output = pygeoconv.esri_json_to_geojson(inp)

        self.assertEqual(output.get("coordinates"), [
            [
                [
                    [-122.63, 45.52],
                    [-122.64, 45.49],
                    [-122.49, 45.48],
                    [-122.52, 45.5],
                    [-122.57, 45.53],
                    [-122.63, 45.52]
                ]
            ],
            [
                [
                    [-83, 35],
                    [-74, 35],
                    [-74, 41],
                    [-83, 41],
                    [-83, 35]
                ]
            ]
        ])

        self.assertEqual(output.get("type"), 'MultiPolygon')

    def test_multipolygon(self):
        inp = {
            type: 'Polygon',
            "rings": [
                [
                    [-100.74462180954974, 39.95017165502381],
                    [-94.50439384003792, 39.91647453608879],
                    [-94.41650267263967, 34.89313438177965],
                    [-100.78856739324887, 34.85708140996771],
                    [-100.74462180954974, 39.95017165502381]
                ],
                [
                    [-99.68993678392353, 39.341088433448896],
                    [-99.68993678392353, 38.24507658785885],
                    [-98.67919734199646, 37.86444431771113],
                    [-98.06395917020868, 38.210554846669694],
                    [-98.06395917020868, 39.341088433448896],
                    [-99.68993678392353, 39.341088433448896]
                ],
                [
                    [-96.83349180978595, 37.23732027507514],
                    [-97.31689323047635, 35.967330282988534],
                    [-96.5698183075912, 35.57512048069255],
                    [-95.42724211456674, 36.357601429255965],
                    [-96.83349180978595, 37.23732027507514]
                ],
                [
                    [-101.4916967324349, 38.24507658785885],
                    [-101.44775114873578, 36.073960493943744],
                    [-103.95263145328033, 36.03843312329154],
                    [-103.68895795108557, 38.03770050767439],
                    [-101.4916967324349, 38.24507658785885]
                ]
            ],
            "spatialReference": {
                "wkid": 4326
            }
        }

        output = pygeoconv.esri_json_to_geojson(inp)

        self.assertEqual(output.get("coordinates"), [
            [
                [[-100.74462180954974, 39.95017165502381], [-100.78856739324887, 34.85708140996771],
                 [-94.41650267263967, 34.89313438177965], [-94.50439384003792, 39.91647453608879],
                 [-100.74462180954974, 39.95017165502381]],
                [[-96.83349180978595, 37.23732027507514], [-95.42724211456674, 36.357601429255965],
                 [-96.5698183075912, 35.57512048069255], [-97.31689323047635, 35.967330282988534],
                 [-96.83349180978595, 37.23732027507514]],
                [[-99.68993678392353, 39.341088433448896], [-98.06395917020868, 39.341088433448896],
                 [-98.06395917020868, 38.210554846669694], [-98.67919734199646, 37.86444431771113],
                 [-99.68993678392353, 38.24507658785885], [-99.68993678392353, 39.341088433448896]]
            ],
            [
                [[-101.4916967324349, 38.24507658785885], [-103.68895795108557, 38.03770050767439],
                 [-103.95263145328033, 36.03843312329154], [-101.44775114873578, 36.073960493943744],
                 [-101.4916967324349, 38.24507658785885]]
            ]
        ])

        self.assertEqual(output.get("type"), 'MultiPolygon')

    def test_holes_outside_rings(self):
        inp = {
            "rings": [
                [[-122.45, 45.63], [-122.45, 45.68], [-122.39, 45.68], [-122.39, 45.63], [-122.45, 45.63]],
                [[-122.46, 45.64], [-122.4, 45.64], [-122.4, 45.66], [-122.46, 45.66], [-122.46, 45.64]]
            ]
        }

        output = pygeoconv.esri_json_to_geojson(inp)

        expected = [
            [[-122.45, 45.63], [-122.39, 45.63], [-122.39, 45.68], [-122.45, 45.68], [-122.45, 45.63]],
            [[-122.46, 45.64], [-122.46, 45.66], [-122.4, 45.66], [-122.4, 45.64], [-122.46, 45.64]]
        ]

        self.assertEqual(output.get("coordinates"), expected)

    def test_feature(self):
        inp = {
            "geometry": {
                "rings": [
                    [[41.8359375, 71.015625],
                     [56.953125, 33.75],
                     [21.796875, 36.5625],
                     [41.8359375, 71.015625]]
                ],
                "spatialReference": {
                    "wkid": 4326
                }
            },
            "attributes": {
                "foo": 'bar'
            }
        }

        output = pygeoconv.esri_json_to_geojson(inp)

        self.assertEqual(output.get("geometry").get("coordinates"), [
            [[41.8359375, 71.015625],
             [21.796875, 36.5625],
             [56.953125, 33.75],
             [41.8359375, 71.015625]]
        ])

        self.assertEqual(output.get("geometry").get("type"), 'Polygon')

    def test_feature_list_to_featurecollection(self):
        inp = {
            "displayFieldName": 'prop0',
            "fieldAliases": {"prop0": 'prop0'},
            "geometryType": 'esriGeometryPolygon',
            "fields": [
                {
                    "name": 'prop0',
                    "type": 'esriFieldTypeString',
                    "alias": 'prop0',
                    "length": 20
                },
                {
                    "name": 'OBJECTID',
                    "type": 'esriFieldTypeOID',
                    "alias": 'OBJECTID'
                },
                {
                    "name": 'FID',
                    "type": 'esriFieldTypeDouble',
                    "alias": 'FID'
                }
            ],
            "spatialReference": {"wkid": 4326},
            "features": [
                {
                    "geometry": {
                        "x": 102,
                        "y": 0.5
                    },
                    "attributes": {
                        "prop0": 'value0',
                        "OBJECTID": 0,
                        "FID": 0
                    }
                }, {
                    "geometry": {
                        "paths": [
                            [[102, 0],
                             [103, 1],
                             [104, 0],
                             [105, 1]]
                        ]
                    },
                    "attributes": {
                        "prop0": None,
                        "OBJECTID": None,
                        "FID": 1
                    }
                }, {
                    "geometry": {
                        "rings": [
                            [[100, 0],
                             [100, 1],
                             [101, 1],
                             [101, 0],
                             [100, 0]]
                        ]
                    },
                    "attributes": {
                        "prop0": None,
                        "OBJECTID": 2,
                        "FID": 30.25
                    }
                }
            ]
        }

        output = pygeoconv.esri_json_to_geojson(inp, 'prop0')

        self.assertEqual(output, {
            "type": 'FeatureCollection',
            "features": [{
                "type": 'Feature',
                "geometry": {
                    "type": 'Point',
                    "coordinates": [102.0, 0.5]
                },
                "properties": {
                    "prop0": 'value0',
                    "OBJECTID": 0,
                    "FID": 0
                },
                "id": 'value0'
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
                    "prop0": None,
                    "OBJECTID": None,
                    "FID": 1
                },
                "id": 1
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
                    "prop0": None,
                    "OBJECTID": 2,
                    "FID": 30.25
                },
                "id": 2
            }]
        })

    def test_feature_with_objectid(self):
        inp = {
            "geometry": {
                "rings": [
                    [[41.8359375, 71.015625],
                     [56.953125, 33.75],
                     [21.796875, 36.5625],
                     [41.8359375, 71.015625]]
                ],
                "spatialReference": {
                    "wkid": 4326
                }
            },
            "attributes": {
                "OBJECTID": 123
            }
        }

        output = pygeoconv.esri_json_to_geojson(inp)

        self.assertEqual(output.get("id"), 123)

    def test_feature_with_fid(self):
        inp = {
            "geometry": {
                "rings": [
                    [[41.8359375, 71.015625],
                     [56.953125, 33.75],
                     [21.796875, 36.5625],
                     [41.8359375, 71.015625]]
                ],
                "spatialReference": {
                    "wkid": 4326
                }
            },
            "attributes": {
                "FID": 123
            }
        }

        output = pygeoconv.esri_json_to_geojson(inp)

        self.assertEqual(output.get("id"), 123)

    def test_feature_with_custom_id(self):
        inp = {
            "geometry": {
                "rings": [
                    [[41.8359375, 71.015625],
                     [56.953125, 33.75],
                     [21.796875, 36.5625],
                     [41.8359375, 71.015625]]
                ],
                "spatialReference": {
                    "wkid": 4326
                }
            },
            "attributes": {
                "FooId": 123
            }
        }

        output = pygeoconv.esri_json_to_geojson(inp, 'FooId')

        self.assertEqual(output.get("id"), 123)

    def test_feature_with_empty_attributes(self):
        inp = {
            "geometry": {
                "rings": [
                    [[41.8359375, 71.015625],
                     [56.953125, 33.75],
                     [21.796875, 36.5625],
                     [41.8359375, 71.015625]]
                ],
                "spatialReference": {
                    "wkid": 4326
                }
            },
            "attributes": {}
        }

        output = pygeoconv.esri_json_to_geojson(inp)

        self.assertEqual(output.get("geometry").get("coordinates"), [
            [
                [41.8359375, 71.015625],
                [21.796875, 36.5625],
                [56.953125, 33.75],
                [41.8359375, 71.015625]
            ]
        ])

        self.assertEqual(output.get("geometry").get("type"), 'Polygon')

    def test_feature_without_attributes(self):
        inp = {
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
            }
        }

        output = pygeoconv.esri_json_to_geojson(inp)

        self.assertEqual(output.get("geometry").get("type"), 'Polygon')
        self.assertEqual(output.get("properties"), {})
        self.assertEqual(output.get("geometry").get("coordinates"), [
            [
                [41.8359375, 71.015625],
                [21.796875, 36.5625],
                [56.953125, 33.75],
                [41.8359375, 71.015625]
            ]
        ])

    def test_feature_with_no_geometry(self):
        inp = {
            "attributes": {
                "foo": 'bar'
            }
        }

        output = pygeoconv.esri_json_to_geojson(inp)

        self.assertEqual(output.get("geometry"), None)
        self.assertEqual(output.get("properties").get("foo"), 'bar')

    def test_feature_id(self):
        inp = {
            "geometry": {
                "x": -66.796875,
                "y": 20.0390625,
                "spatialReference": {
                    "wkid": 4326
                }
            },
            "attributes": {
                "OBJECTID": 123,
                "some_field": {
                    'not an number': 'or a string'
                }
            }
        }

        output = pygeoconv.esri_json_to_geojson(inp, 'some_field')

        # 'some_field' is not a number - fallback to OBJECTID
        self.assertEqual(output.get("id"), 123)

    def test_custom_objectid(self):
        inp = {
            "geometry": {
                "x": -66.796875,
                "y": 20.0390625,
                "spatialReference": {
                    "wkid": 4326
                }
            },
            "attributes": {
                "OBJECTID": 123,
                "otherIdField": 456
            }
        }

        output = pygeoconv.esri_json_to_geojson(inp, 'otherIdField')

        # otherIdField as id
        self.assertEqual(output.get("id"), 456)

    def test_feature_with_undefined_objectid(self):
        inp = {
            "geometry": {
                "x": -66.796875,
                "y": 20.0390625,
                "spatialReference": {
                    "wkid": 4326
                }
            },

            "attributes": {
                "foo": 'bar'
            }
        }

        output = pygeoconv.esri_json_to_geojson(inp)

        # output should not have an id key
        self.assertTrue("id" not in output)

    def test_should_not_modify_original_geometry(self):
        inp = {
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
                "foo": 'bar'
            }
        }

        original = json.dumps(inp)

        pygeoconv.esri_json_to_geojson(inp)

        self.assertEqual(original, json.dumps(inp))

    def test_extent(self):
        inp = {
            "xmax": -35.5078125,
            "ymax": 41.244772343082076,
            "xmin": -13.7109375,
            "ymin": 54.36775852406841,
            "spatialReference": {
                "wkid": 4326
            }
        }

        output = pygeoconv.esri_json_to_geojson(inp)

        self.assertEqual(output.get("coordinates"), [
            [[-35.5078125, 41.244772343082076], [-13.7109375, 41.244772343082076], [-13.7109375, 54.36775852406841],
             [-35.5078125, 54.36775852406841], [-35.5078125, 41.244772343082076]]])
        self.assertEqual(output.get("type"), 'Polygon')

    def test_extent_empty(self):
        inp = {
            "xmax": "NaN",
            "ymax": "NaN",
            "xmin": "NaN",
            "ymin": "NaN",
            "spatialReference": {
                "wkid": 4326
            }
        }

        output = pygeoconv.esri_json_to_geojson(inp)

        self.assertEqual(output.get("coordinates"), [])
        self.assertEqual(output.get("type"), 'Polygon')

    def test_unknown_object(self):
        inp = {
            "someAttr": None
        }
        with self.assertRaises(EsriJsonParserError):
            pygeoconv.esri_json_to_geojson(inp)
