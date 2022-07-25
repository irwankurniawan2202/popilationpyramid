{
  "$schema": "https://vega.github.io/schema/vega/v5.json",
  "description": "A population pyramid showing U.S. demographics from 1850 to 2000.",
  "height": "container",
  "padding": 5,
  "signals": [
    {
      "name": "chartWidth",
      "value": 300
    },
    {
      "name": "chartPad",
      "value": 20
    },
    {
      "name": "width",
      "update": "2 * chartWidth + chartPad"
    },
    {
      "name": "year",
      "value": 2000,
      "bind": {
        "input": "range",
        "min": 1850,
        "max": 2000,
        "step": 10
      }
    }
  ],
  "data": [
    {
      "name": "population",
      "format": {
        "property": "aggregations.eqpt_buckets.buckets"
      },
      "url": {
        "index": "population",
        "body": {
          "aggs": {
            "eqpt_buckets": {
              "composite": {
                "size": 5000,
                "sources": [
                  {
                    "year": {
                      "terms": {
                        "field": "year"
                      }
                    }
                  },
                  {
                    "sex": {
                      "terms": {
                        "field": "sex"
                      }
                    }
                  },
                  {
                    "age": {
                      "terms": {
                        "field": "age"
                      }
                    }
                  },
                  {
                    "people": {
                      "terms": {
                        "field": "people"
                      }
                    }
                  }
                ]
              }
            }
          },
          "query": {
            "bool": {
              "must": [],
              "filter": [],
              "should": [],
              "must_not": []
            }
          }
        }
      },
      "values": {
        "took": 12,
        "timed_out": false,
        "_shards": {
          "total": 1,
          "successful": 1,
          "skipped": 0,
          "failed": 0
        },
        "hits": {
          "total": 570,
          "max_score": 1,
          "hits": [
            {
              "_index": "population",
              "_type": "_doc",
              "_id": "k2CrEIIBc4t5Qvm_Mk11",
              "_score": 1,
              "_source": {
                "year": 1850,
                "sex": 1,
                "people": 1483789,
                "age": 0
              }
            },
            {
              "_index": "population",
              "_type": "_doc",
              "_id": "lGCrEIIBc4t5Qvm_Mk12",
              "_score": 1,
              "_source": {
                "year": 1850,
                "sex": 2,
                "people": 1450376,
                "age": 0
              }
            },
            {
              "_index": "population",
              "_type": "_doc",
              "_id": "lWCrEIIBc4t5Qvm_Mk12",
              "_score": 1,
              "_source": {
                "year": 1850,
                "sex": 1,
                "people": 1411067,
                "age": 5
              }
            },
            {
              "_index": "population",
              "_type": "_doc",
              "_id": "lmCrEIIBc4t5Qvm_Mk12",
              "_score": 1,
              "_source": {
                "year": 1850,
                "sex": 2,
                "people": 1359668,
                "age": 5
              }
            },
            {
              "_index": "population",
              "_type": "_doc",
              "_id": "l2CrEIIBc4t5Qvm_Mk12",
              "_score": 1,
              "_source": {
                "year": 1850,
                "sex": 1,
                "people": 1260099,
                "age": 10
              }
            },
            {
              "_index": "population",
              "_type": "_doc",
              "_id": "mGCrEIIBc4t5Qvm_Mk12",
              "_score": 1,
              "_source": {
                "year": 1850,
                "sex": 2,
                "people": 1216114,
                "age": 10
              }
            },
            {
              "_index": "population",
              "_type": "_doc",
              "_id": "mWCrEIIBc4t5Qvm_Mk12",
              "_score": 1,
              "_source": {
                "year": 1850,
                "sex": 1,
                "people": 1077133,
                "age": 15
              }
            },
            {
              "_index": "population",
              "_type": "_doc",
              "_id": "mmCrEIIBc4t5Qvm_Mk12",
              "_score": 1,
              "_source": {
                "year": 1850,
                "sex": 2,
                "people": 1110619,
                "age": 15
              }
            },
            {
              "_index": "population",
              "_type": "_doc",
              "_id": "m2CrEIIBc4t5Qvm_Mk12",
              "_score": 1,
              "_source": {
                "year": 1850,
                "sex": 1,
                "people": 1017281,
                "age": 20
              }
            },
            {
              "_index": "population",
              "_type": "_doc",
              "_id": "nGCrEIIBc4t5Qvm_Mk12",
              "_score": 1,
              "_source": {
                "year": 1850,
                "sex": 2,
                "people": 1003841,
                "age": 20
              }
            }
          ]
        },
        "aggregations": {
          "eqpt_buckets": {
            "after_key": {
              "year": 2000,
              "sex": 2,
              "age": 90,
              "people": 1064581
            },
            "buckets": [
              {
                "key": {
                  "year": 1850,
                  "sex": 1,
                  "age": 0,
                  "people": 1483789
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1850,
                  "sex": 1,
                  "age": 5,
                  "people": 1411067
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1850,
                  "sex": 1,
                  "age": 10,
                  "people": 1260099
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1850,
                  "sex": 1,
                  "age": 15,
                  "people": 1077133
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1850,
                  "sex": 1,
                  "age": 20,
                  "people": 1017281
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1850,
                  "sex": 1,
                  "age": 25,
                  "people": 862547
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1850,
                  "sex": 1,
                  "age": 30,
                  "people": 730638
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1850,
                  "sex": 1,
                  "age": 35,
                  "people": 588487
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1850,
                  "sex": 1,
                  "age": 40,
                  "people": 475911
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1850,
                  "sex": 1,
                  "age": 45,
                  "people": 384211
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1850,
                  "sex": 1,
                  "age": 50,
                  "people": 321343
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1850,
                  "sex": 1,
                  "age": 55,
                  "people": 194080
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1850,
                  "sex": 1,
                  "age": 60,
                  "people": 174976
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1850,
                  "sex": 1,
                  "age": 65,
                  "people": 106827
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1850,
                  "sex": 1,
                  "age": 70,
                  "people": 73677
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1850,
                  "sex": 1,
                  "age": 75,
                  "people": 40834
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1850,
                  "sex": 1,
                  "age": 80,
                  "people": 23449
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1850,
                  "sex": 1,
                  "age": 85,
                  "people": 8186
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1850,
                  "sex": 1,
                  "age": 90,
                  "people": 5259
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1850,
                  "sex": 2,
                  "age": 0,
                  "people": 1450376
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1850,
                  "sex": 2,
                  "age": 5,
                  "people": 1359668
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1850,
                  "sex": 2,
                  "age": 10,
                  "people": 1216114
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1850,
                  "sex": 2,
                  "age": 15,
                  "people": 1110619
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1850,
                  "sex": 2,
                  "age": 20,
                  "people": 1003841
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1850,
                  "sex": 2,
                  "age": 25,
                  "people": 799482
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1850,
                  "sex": 2,
                  "age": 30,
                  "people": 639636
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1850,
                  "sex": 2,
                  "age": 35,
                  "people": 505012
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1850,
                  "sex": 2,
                  "age": 40,
                  "people": 428185
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1850,
                  "sex": 2,
                  "age": 45,
                  "people": 341254
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1850,
                  "sex": 2,
                  "age": 50,
                  "people": 286580
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1850,
                  "sex": 2,
                  "age": 55,
                  "people": 187208
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1850,
                  "sex": 2,
                  "age": 60,
                  "people": 162236
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1850,
                  "sex": 2,
                  "age": 65,
                  "people": 105534
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1850,
                  "sex": 2,
                  "age": 70,
                  "people": 71762
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1850,
                  "sex": 2,
                  "age": 75,
                  "people": 40229
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1850,
                  "sex": 2,
                  "age": 80,
                  "people": 22949
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1850,
                  "sex": 2,
                  "age": 85,
                  "people": 10511
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1850,
                  "sex": 2,
                  "age": 90,
                  "people": 6569
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1860,
                  "sex": 1,
                  "age": 0,
                  "people": 2120846
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1860,
                  "sex": 1,
                  "age": 5,
                  "people": 1804467
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1860,
                  "sex": 1,
                  "age": 10,
                  "people": 1612640
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1860,
                  "sex": 1,
                  "age": 15,
                  "people": 1438094
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1860,
                  "sex": 1,
                  "age": 20,
                  "people": 1351121
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1860,
                  "sex": 1,
                  "age": 25,
                  "people": 1217615
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1860,
                  "sex": 1,
                  "age": 30,
                  "people": 1043174
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1860,
                  "sex": 1,
                  "age": 35,
                  "people": 866910
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1860,
                  "sex": 1,
                  "age": 40,
                  "people": 699434
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1860,
                  "sex": 1,
                  "age": 45,
                  "people": 552404
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1860,
                  "sex": 1,
                  "age": 50,
                  "people": 456176
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1860,
                  "sex": 1,
                  "age": 55,
                  "people": 292417
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1860,
                  "sex": 1,
                  "age": 60,
                  "people": 260887
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1860,
                  "sex": 1,
                  "age": 65,
                  "people": 149331
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1860,
                  "sex": 1,
                  "age": 70,
                  "people": 98465
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1860,
                  "sex": 1,
                  "age": 75,
                  "people": 56699
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1860,
                  "sex": 1,
                  "age": 80,
                  "people": 29007
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1860,
                  "sex": 1,
                  "age": 85,
                  "people": 10434
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1860,
                  "sex": 1,
                  "age": 90,
                  "people": 7232
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1860,
                  "sex": 2,
                  "age": 0,
                  "people": 2092162
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1860,
                  "sex": 2,
                  "age": 5,
                  "people": 1778772
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1860,
                  "sex": 2,
                  "age": 10,
                  "people": 1540350
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1860,
                  "sex": 2,
                  "age": 15,
                  "people": 1495999
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1860,
                  "sex": 2,
                  "age": 20,
                  "people": 1370462
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1860,
                  "sex": 2,
                  "age": 25,
                  "people": 1116373
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1860,
                  "sex": 2,
                  "age": 30,
                  "people": 936055
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1860,
                  "sex": 2,
                  "age": 35,
                  "people": 737136
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1860,
                  "sex": 2,
                  "age": 40,
                  "people": 616826
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1860,
                  "sex": 2,
                  "age": 45,
                  "people": 461739
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1860,
                  "sex": 2,
                  "age": 50,
                  "people": 407305
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1860,
                  "sex": 2,
                  "age": 55,
                  "people": 267224
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1860,
                  "sex": 2,
                  "age": 60,
                  "people": 249735
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1860,
                  "sex": 2,
                  "age": 65,
                  "people": 141405
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1860,
                  "sex": 2,
                  "age": 70,
                  "people": 101778
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1860,
                  "sex": 2,
                  "age": 75,
                  "people": 57597
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1860,
                  "sex": 2,
                  "age": 80,
                  "people": 29506
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1860,
                  "sex": 2,
                  "age": 85,
                  "people": 14053
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1860,
                  "sex": 2,
                  "age": 90,
                  "people": 6622
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1870,
                  "sex": 1,
                  "age": 0,
                  "people": 2800083
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1870,
                  "sex": 1,
                  "age": 5,
                  "people": 2428469
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1870,
                  "sex": 1,
                  "age": 10,
                  "people": 2427341
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1870,
                  "sex": 1,
                  "age": 15,
                  "people": 1958390
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1870,
                  "sex": 1,
                  "age": 20,
                  "people": 1805303
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1870,
                  "sex": 1,
                  "age": 25,
                  "people": 1509059
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1870,
                  "sex": 1,
                  "age": 30,
                  "people": 1251534
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1870,
                  "sex": 1,
                  "age": 35,
                  "people": 1185336
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1870,
                  "sex": 1,
                  "age": 40,
                  "people": 968861
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1870,
                  "sex": 1,
                  "age": 45,
                  "people": 852672
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1870,
                  "sex": 1,
                  "age": 50,
                  "people": 736387
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1870,
                  "sex": 1,
                  "age": 55,
                  "people": 486036
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1870,
                  "sex": 1,
                  "age": 60,
                  "people": 399264
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1870,
                  "sex": 1,
                  "age": 65,
                  "people": 260829
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1870,
                  "sex": 1,
                  "age": 70,
                  "people": 173364
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1870,
                  "sex": 1,
                  "age": 75,
                  "people": 86929
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1870,
                  "sex": 1,
                  "age": 80,
                  "people": 47427
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1870,
                  "sex": 1,
                  "age": 85,
                  "people": 15891
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1870,
                  "sex": 1,
                  "age": 90,
                  "people": 8649
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1870,
                  "sex": 2,
                  "age": 0,
                  "people": 2717102
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1870,
                  "sex": 2,
                  "age": 5,
                  "people": 2393680
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1870,
                  "sex": 2,
                  "age": 10,
                  "people": 2342670
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1870,
                  "sex": 2,
                  "age": 15,
                  "people": 2077248
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1870,
                  "sex": 2,
                  "age": 20,
                  "people": 1909382
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1870,
                  "sex": 2,
                  "age": 25,
                  "people": 1574285
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1870,
                  "sex": 2,
                  "age": 30,
                  "people": 1275629
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1870,
                  "sex": 2,
                  "age": 35,
                  "people": 1137490
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1870,
                  "sex": 2,
                  "age": 40,
                  "people": 944401
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1870,
                  "sex": 2,
                  "age": 45,
                  "people": 747916
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1870,
                  "sex": 2,
                  "age": 50,
                  "people": 637801
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1870,
                  "sex": 2,
                  "age": 55,
                  "people": 407819
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1870,
                  "sex": 2,
                  "age": 60,
                  "people": 374801
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1870,
                  "sex": 2,
                  "age": 65,
                  "people": 239080
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1870,
                  "sex": 2,
                  "age": 70,
                  "people": 165501
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1870,
                  "sex": 2,
                  "age": 75,
                  "people": 89540
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1870,
                  "sex": 2,
                  "age": 80,
                  "people": 54190
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1870,
                  "sex": 2,
                  "age": 85,
                  "people": 19302
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1870,
                  "sex": 2,
                  "age": 90,
                  "people": 13068
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1880,
                  "sex": 1,
                  "age": 0,
                  "people": 3533662
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1880,
                  "sex": 1,
                  "age": 5,
                  "people": 3297503
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1880,
                  "sex": 1,
                  "age": 10,
                  "people": 2911924
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1880,
                  "sex": 1,
                  "age": 15,
                  "people": 2457734
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1880,
                  "sex": 1,
                  "age": 20,
                  "people": 2547780
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1880,
                  "sex": 1,
                  "age": 25,
                  "people": 2119393
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1880,
                  "sex": 1,
                  "age": 30,
                  "people": 1749107
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1880,
                  "sex": 1,
                  "age": 35,
                  "people": 1540772
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1880,
                  "sex": 1,
                  "age": 40,
                  "people": 1237347
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1880,
                  "sex": 1,
                  "age": 45,
                  "people": 1065973
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1880,
                  "sex": 1,
                  "age": 50,
                  "people": 964484
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1880,
                  "sex": 1,
                  "age": 55,
                  "people": 679147
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1880,
                  "sex": 1,
                  "age": 60,
                  "people": 580298
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1880,
                  "sex": 1,
                  "age": 65,
                  "people": 369398
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1880,
                  "sex": 1,
                  "age": 70,
                  "people": 255422
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1880,
                  "sex": 1,
                  "age": 75,
                  "people": 141628
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1880,
                  "sex": 1,
                  "age": 80,
                  "people": 67526
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1880,
                  "sex": 1,
                  "age": 85,
                  "people": 22437
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1880,
                  "sex": 1,
                  "age": 90,
                  "people": 10272
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1880,
                  "sex": 2,
                  "age": 0,
                  "people": 3421597
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1880,
                  "sex": 2,
                  "age": 5,
                  "people": 3179142
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1880,
                  "sex": 2,
                  "age": 10,
                  "people": 2813550
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1880,
                  "sex": 2,
                  "age": 15,
                  "people": 2527818
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1880,
                  "sex": 2,
                  "age": 20,
                  "people": 2512803
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1880,
                  "sex": 2,
                  "age": 25,
                  "people": 1974241
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1880,
                  "sex": 2,
                  "age": 30,
                  "people": 1596772
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1880,
                  "sex": 2,
                  "age": 35,
                  "people": 1483717
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1880,
                  "sex": 2,
                  "age": 40,
                  "people": 1239435
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1880,
                  "sex": 2,
                  "age": 45,
                  "people": 1003711
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1880,
                  "sex": 2,
                  "age": 50,
                  "people": 863012
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1880,
                  "sex": 2,
                  "age": 55,
                  "people": 594843
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1880,
                  "sex": 2,
                  "age": 60,
                  "people": 526956
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1880,
                  "sex": 2,
                  "age": 65,
                  "people": 346303
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1880,
                  "sex": 2,
                  "age": 70,
                  "people": 251860
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1880,
                  "sex": 2,
                  "age": 75,
                  "people": 143513
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1880,
                  "sex": 2,
                  "age": 80,
                  "people": 77290
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1880,
                  "sex": 2,
                  "age": 85,
                  "people": 31227
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1880,
                  "sex": 2,
                  "age": 90,
                  "people": 15451
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1900,
                  "sex": 1,
                  "age": 0,
                  "people": 4619544
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1900,
                  "sex": 1,
                  "age": 5,
                  "people": 4465783
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1900,
                  "sex": 1,
                  "age": 10,
                  "people": 4057669
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1900,
                  "sex": 1,
                  "age": 15,
                  "people": 3774846
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1900,
                  "sex": 1,
                  "age": 20,
                  "people": 3694038
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1900,
                  "sex": 1,
                  "age": 25,
                  "people": 3389280
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1900,
                  "sex": 1,
                  "age": 30,
                  "people": 2918964
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1900,
                  "sex": 1,
                  "age": 35,
                  "people": 2633883
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1900,
                  "sex": 1,
                  "age": 40,
                  "people": 2261070
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1900,
                  "sex": 1,
                  "age": 45,
                  "people": 1868413
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1900,
                  "sex": 1,
                  "age": 50,
                  "people": 1571038
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1900,
                  "sex": 1,
                  "age": 55,
                  "people": 1161908
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1900,
                  "sex": 1,
                  "age": 60,
                  "people": 916571
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1900,
                  "sex": 1,
                  "age": 65,
                  "people": 672663
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1900,
                  "sex": 1,
                  "age": 70,
                  "people": 454747
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1900,
                  "sex": 1,
                  "age": 75,
                  "people": 268211
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1900,
                  "sex": 1,
                  "age": 80,
                  "people": 127435
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1900,
                  "sex": 1,
                  "age": 85,
                  "people": 44008
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1900,
                  "sex": 1,
                  "age": 90,
                  "people": 15164
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1900,
                  "sex": 2,
                  "age": 0,
                  "people": 4589196
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1900,
                  "sex": 2,
                  "age": 5,
                  "people": 4390483
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1900,
                  "sex": 2,
                  "age": 10,
                  "people": 4001749
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1900,
                  "sex": 2,
                  "age": 15,
                  "people": 3801743
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1900,
                  "sex": 2,
                  "age": 20,
                  "people": 3751061
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1900,
                  "sex": 2,
                  "age": 25,
                  "people": 3236056
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1900,
                  "sex": 2,
                  "age": 30,
                  "people": 2665174
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1900,
                  "sex": 2,
                  "age": 35,
                  "people": 2347737
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1900,
                  "sex": 2,
                  "age": 40,
                  "people": 2004987
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1900,
                  "sex": 2,
                  "age": 45,
                  "people": 1648025
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1900,
                  "sex": 2,
                  "age": 50,
                  "people": 1411981
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1900,
                  "sex": 2,
                  "age": 55,
                  "people": 1064632
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1900,
                  "sex": 2,
                  "age": 60,
                  "people": 887508
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1900,
                  "sex": 2,
                  "age": 65,
                  "people": 640212
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1900,
                  "sex": 2,
                  "age": 70,
                  "people": 440007
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1900,
                  "sex": 2,
                  "age": 75,
                  "people": 265879
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1900,
                  "sex": 2,
                  "age": 80,
                  "people": 132449
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1900,
                  "sex": 2,
                  "age": 85,
                  "people": 48614
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1900,
                  "sex": 2,
                  "age": 90,
                  "people": 20093
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1910,
                  "sex": 1,
                  "age": 0,
                  "people": 5296823
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1910,
                  "sex": 1,
                  "age": 5,
                  "people": 4991803
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1910,
                  "sex": 1,
                  "age": 10,
                  "people": 4650747
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1910,
                  "sex": 1,
                  "age": 15,
                  "people": 4566154
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1910,
                  "sex": 1,
                  "age": 20,
                  "people": 4637632
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1910,
                  "sex": 1,
                  "age": 25,
                  "people": 4257755
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1910,
                  "sex": 1,
                  "age": 30,
                  "people": 3658125
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1910,
                  "sex": 1,
                  "age": 35,
                  "people": 3427518
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1910,
                  "sex": 1,
                  "age": 40,
                  "people": 2860229
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1910,
                  "sex": 1,
                  "age": 45,
                  "people": 2363801
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1910,
                  "sex": 1,
                  "age": 50,
                  "people": 2126516
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1910,
                  "sex": 1,
                  "age": 55,
                  "people": 1508358
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1910,
                  "sex": 1,
                  "age": 60,
                  "people": 1189421
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1910,
                  "sex": 1,
                  "age": 65,
                  "people": 850159
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1910,
                  "sex": 1,
                  "age": 70,
                  "people": 557936
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1910,
                  "sex": 1,
                  "age": 75,
                  "people": 322679
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1910,
                  "sex": 1,
                  "age": 80,
                  "people": 161715
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1910,
                  "sex": 1,
                  "age": 85,
                  "people": 59699
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1910,
                  "sex": 1,
                  "age": 90,
                  "people": 23929
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1910,
                  "sex": 2,
                  "age": 0,
                  "people": 5287477
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1910,
                  "sex": 2,
                  "age": 5,
                  "people": 4866139
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1910,
                  "sex": 2,
                  "age": 10,
                  "people": 4471887
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1910,
                  "sex": 2,
                  "age": 15,
                  "people": 4592269
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1910,
                  "sex": 2,
                  "age": 20,
                  "people": 4447683
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1910,
                  "sex": 2,
                  "age": 25,
                  "people": 3946153
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1910,
                  "sex": 2,
                  "age": 30,
                  "people": 3295220
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1910,
                  "sex": 2,
                  "age": 35,
                  "people": 3088990
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1910,
                  "sex": 2,
                  "age": 40,
                  "people": 2471267
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1910,
                  "sex": 2,
                  "age": 45,
                  "people": 2114930
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1910,
                  "sex": 2,
                  "age": 50,
                  "people": 1773592
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1910,
                  "sex": 2,
                  "age": 55,
                  "people": 1317651
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1910,
                  "sex": 2,
                  "age": 60,
                  "people": 1090697
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1910,
                  "sex": 2,
                  "age": 65,
                  "people": 813868
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1910,
                  "sex": 2,
                  "age": 70,
                  "people": 547623
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1910,
                  "sex": 2,
                  "age": 75,
                  "people": 350900
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1910,
                  "sex": 2,
                  "age": 80,
                  "people": 174315
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1910,
                  "sex": 2,
                  "age": 85,
                  "people": 62725
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1910,
                  "sex": 2,
                  "age": 90,
                  "people": 28965
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1920,
                  "sex": 1,
                  "age": 0,
                  "people": 5934792
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1920,
                  "sex": 1,
                  "age": 5,
                  "people": 5789008
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1920,
                  "sex": 1,
                  "age": 10,
                  "people": 5401156
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1920,
                  "sex": 1,
                  "age": 15,
                  "people": 4724365
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1920,
                  "sex": 1,
                  "age": 20,
                  "people": 4549411
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1920,
                  "sex": 1,
                  "age": 25,
                  "people": 4565066
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1920,
                  "sex": 1,
                  "age": 30,
                  "people": 4110771
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1920,
                  "sex": 1,
                  "age": 35,
                  "people": 4081543
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1920,
                  "sex": 1,
                  "age": 40,
                  "people": 3321923
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1920,
                  "sex": 1,
                  "age": 45,
                  "people": 3143891
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1920,
                  "sex": 1,
                  "age": 50,
                  "people": 2546035
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1920,
                  "sex": 1,
                  "age": 55,
                  "people": 1880975
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1920,
                  "sex": 1,
                  "age": 60,
                  "people": 1587549
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1920,
                  "sex": 1,
                  "age": 65,
                  "people": 1095956
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1920,
                  "sex": 1,
                  "age": 70,
                  "people": 714618
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1920,
                  "sex": 1,
                  "age": 75,
                  "people": 417292
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1920,
                  "sex": 1,
                  "age": 80,
                  "people": 187000
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1920,
                  "sex": 1,
                  "age": 85,
                  "people": 75991
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1920,
                  "sex": 1,
                  "age": 90,
                  "people": 22398
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1920,
                  "sex": 2,
                  "age": 0,
                  "people": 5694244
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1920,
                  "sex": 2,
                  "age": 5,
                  "people": 5693960
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1920,
                  "sex": 2,
                  "age": 10,
                  "people": 5293057
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1920,
                  "sex": 2,
                  "age": 15,
                  "people": 4779936
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1920,
                  "sex": 2,
                  "age": 20,
                  "people": 4742632
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1920,
                  "sex": 2,
                  "age": 25,
                  "people": 4529382
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1920,
                  "sex": 2,
                  "age": 30,
                  "people": 3982426
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1920,
                  "sex": 2,
                  "age": 35,
                  "people": 3713810
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1920,
                  "sex": 2,
                  "age": 40,
                  "people": 3059757
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1920,
                  "sex": 2,
                  "age": 45,
                  "people": 2669089
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1920,
                  "sex": 2,
                  "age": 50,
                  "people": 2200491
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1920,
                  "sex": 2,
                  "age": 55,
                  "people": 1674672
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1920,
                  "sex": 2,
                  "age": 60,
                  "people": 1382877
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1920,
                  "sex": 2,
                  "age": 65,
                  "people": 989901
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1920,
                  "sex": 2,
                  "age": 70,
                  "people": 690097
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1920,
                  "sex": 2,
                  "age": 75,
                  "people": 439465
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1920,
                  "sex": 2,
                  "age": 80,
                  "people": 211110
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1920,
                  "sex": 2,
                  "age": 85,
                  "people": 92829
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1920,
                  "sex": 2,
                  "age": 90,
                  "people": 32085
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1930,
                  "sex": 1,
                  "age": 0,
                  "people": 5875250
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1930,
                  "sex": 1,
                  "age": 5,
                  "people": 6542592
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1930,
                  "sex": 1,
                  "age": 10,
                  "people": 6064820
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1930,
                  "sex": 1,
                  "age": 15,
                  "people": 5709452
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1930,
                  "sex": 1,
                  "age": 20,
                  "people": 5305992
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1930,
                  "sex": 1,
                  "age": 25,
                  "people": 4929853
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1930,
                  "sex": 1,
                  "age": 30,
                  "people": 4424408
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1930,
                  "sex": 1,
                  "age": 35,
                  "people": 4576531
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1930,
                  "sex": 1,
                  "age": 40,
                  "people": 4075139
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1930,
                  "sex": 1,
                  "age": 45,
                  "people": 3633152
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1930,
                  "sex": 1,
                  "age": 50,
                  "people": 3128108
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1930,
                  "sex": 1,
                  "age": 55,
                  "people": 2434077
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1930,
                  "sex": 1,
                  "age": 60,
                  "people": 1927564
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1930,
                  "sex": 1,
                  "age": 65,
                  "people": 1397275
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1930,
                  "sex": 1,
                  "age": 70,
                  "people": 919045
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1930,
                  "sex": 1,
                  "age": 75,
                  "people": 536375
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1930,
                  "sex": 1,
                  "age": 80,
                  "people": 246708
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1930,
                  "sex": 1,
                  "age": 85,
                  "people": 88978
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1930,
                  "sex": 1,
                  "age": 90,
                  "people": 30338
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1930,
                  "sex": 2,
                  "age": 0,
                  "people": 5662530
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1930,
                  "sex": 2,
                  "age": 5,
                  "people": 6129561
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1930,
                  "sex": 2,
                  "age": 10,
                  "people": 5986529
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1930,
                  "sex": 2,
                  "age": 15,
                  "people": 5769587
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1930,
                  "sex": 2,
                  "age": 20,
                  "people": 5565382
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1930,
                  "sex": 2,
                  "age": 25,
                  "people": 5050229
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1930,
                  "sex": 2,
                  "age": 30,
                  "people": 4455213
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1930,
                  "sex": 2,
                  "age": 35,
                  "people": 4593776
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1930,
                  "sex": 2,
                  "age": 40,
                  "people": 3754022
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1930,
                  "sex": 2,
                  "age": 45,
                  "people": 3396558
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1930,
                  "sex": 2,
                  "age": 50,
                  "people": 2809191
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1930,
                  "sex": 2,
                  "age": 55,
                  "people": 2298614
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1930,
                  "sex": 2,
                  "age": 60,
                  "people": 1783515
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1930,
                  "sex": 2,
                  "age": 65,
                  "people": 1307312
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1930,
                  "sex": 2,
                  "age": 70,
                  "people": 918509
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1930,
                  "sex": 2,
                  "age": 75,
                  "people": 522716
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1930,
                  "sex": 2,
                  "age": 80,
                  "people": 283579
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1930,
                  "sex": 2,
                  "age": 85,
                  "people": 109210
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1930,
                  "sex": 2,
                  "age": 90,
                  "people": 43483
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1940,
                  "sex": 1,
                  "age": 0,
                  "people": 5294628
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1940,
                  "sex": 1,
                  "age": 5,
                  "people": 5468378
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1940,
                  "sex": 1,
                  "age": 10,
                  "people": 5960416
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1940,
                  "sex": 1,
                  "age": 15,
                  "people": 6165109
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1940,
                  "sex": 1,
                  "age": 20,
                  "people": 5682414
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1940,
                  "sex": 1,
                  "age": 25,
                  "people": 5438166
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1940,
                  "sex": 1,
                  "age": 30,
                  "people": 5040048
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1940,
                  "sex": 1,
                  "age": 35,
                  "people": 4724804
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1940,
                  "sex": 1,
                  "age": 40,
                  "people": 4437392
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1940,
                  "sex": 1,
                  "age": 45,
                  "people": 4190187
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1940,
                  "sex": 1,
                  "age": 50,
                  "people": 3785735
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1940,
                  "sex": 1,
                  "age": 55,
                  "people": 2972069
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1940,
                  "sex": 1,
                  "age": 60,
                  "people": 2370232
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1940,
                  "sex": 1,
                  "age": 65,
                  "people": 1897678
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1940,
                  "sex": 1,
                  "age": 70,
                  "people": 1280023
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1940,
                  "sex": 1,
                  "age": 75,
                  "people": 713875
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1940,
                  "sex": 1,
                  "age": 80,
                  "people": 359418
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1940,
                  "sex": 1,
                  "age": 85,
                  "people": 127303
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1940,
                  "sex": 1,
                  "age": 90,
                  "people": 42263
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1940,
                  "sex": 2,
                  "age": 0,
                  "people": 5124653
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1940,
                  "sex": 2,
                  "age": 5,
                  "people": 5359099
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1940,
                  "sex": 2,
                  "age": 10,
                  "people": 5868532
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1940,
                  "sex": 2,
                  "age": 15,
                  "people": 6193701
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1940,
                  "sex": 2,
                  "age": 20,
                  "people": 5896002
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1940,
                  "sex": 2,
                  "age": 25,
                  "people": 5664244
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1940,
                  "sex": 2,
                  "age": 30,
                  "people": 5171522
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1940,
                  "sex": 2,
                  "age": 35,
                  "people": 4791809
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1940,
                  "sex": 2,
                  "age": 40,
                  "people": 4394061
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1940,
                  "sex": 2,
                  "age": 45,
                  "people": 4050290
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1940,
                  "sex": 2,
                  "age": 50,
                  "people": 3488396
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1940,
                  "sex": 2,
                  "age": 55,
                  "people": 2810000
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1940,
                  "sex": 2,
                  "age": 60,
                  "people": 2317790
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1940,
                  "sex": 2,
                  "age": 65,
                  "people": 1911117
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1940,
                  "sex": 2,
                  "age": 70,
                  "people": 1287711
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1940,
                  "sex": 2,
                  "age": 75,
                  "people": 764915
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1940,
                  "sex": 2,
                  "age": 80,
                  "people": 414761
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1940,
                  "sex": 2,
                  "age": 85,
                  "people": 152131
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1940,
                  "sex": 2,
                  "age": 90,
                  "people": 58119
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1950,
                  "sex": 1,
                  "age": 0,
                  "people": 8211806
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1950,
                  "sex": 1,
                  "age": 5,
                  "people": 6706601
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1950,
                  "sex": 1,
                  "age": 10,
                  "people": 5629744
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1950,
                  "sex": 1,
                  "age": 15,
                  "people": 5264129
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1950,
                  "sex": 1,
                  "age": 20,
                  "people": 5573308
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1950,
                  "sex": 1,
                  "age": 25,
                  "people": 6007254
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1950,
                  "sex": 1,
                  "age": 30,
                  "people": 5676022
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1950,
                  "sex": 1,
                  "age": 35,
                  "people": 5511364
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1950,
                  "sex": 1,
                  "age": 40,
                  "people": 5076985
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1950,
                  "sex": 1,
                  "age": 45,
                  "people": 4533177
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1950,
                  "sex": 1,
                  "age": 50,
                  "people": 4199164
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1950,
                  "sex": 1,
                  "age": 55,
                  "people": 3667351
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1950,
                  "sex": 1,
                  "age": 60,
                  "people": 3035038
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1950,
                  "sex": 1,
                  "age": 65,
                  "people": 2421234
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1950,
                  "sex": 1,
                  "age": 70,
                  "people": 1627920
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1950,
                  "sex": 1,
                  "age": 75,
                  "people": 1006530
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1950,
                  "sex": 1,
                  "age": 80,
                  "people": 511727
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1950,
                  "sex": 1,
                  "age": 85,
                  "people": 182821
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1950,
                  "sex": 1,
                  "age": 90,
                  "people": 54836
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1950,
                  "sex": 2,
                  "age": 0,
                  "people": 7862267
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1950,
                  "sex": 2,
                  "age": 5,
                  "people": 6450863
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1950,
                  "sex": 2,
                  "age": 10,
                  "people": 5430835
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1950,
                  "sex": 2,
                  "age": 15,
                  "people": 5288742
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1950,
                  "sex": 2,
                  "age": 20,
                  "people": 5854227
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1950,
                  "sex": 2,
                  "age": 25,
                  "people": 6317332
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1950,
                  "sex": 2,
                  "age": 30,
                  "people": 5895178
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1950,
                  "sex": 2,
                  "age": 35,
                  "people": 5696261
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1950,
                  "sex": 2,
                  "age": 40,
                  "people": 5199224
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1950,
                  "sex": 2,
                  "age": 45,
                  "people": 4595842
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1950,
                  "sex": 2,
                  "age": 50,
                  "people": 4147295
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1950,
                  "sex": 2,
                  "age": 55,
                  "people": 3595158
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1950,
                  "sex": 2,
                  "age": 60,
                  "people": 3009768
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1950,
                  "sex": 2,
                  "age": 65,
                  "people": 2548250
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1950,
                  "sex": 2,
                  "age": 70,
                  "people": 1786831
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1950,
                  "sex": 2,
                  "age": 75,
                  "people": 1148469
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1950,
                  "sex": 2,
                  "age": 80,
                  "people": 637717
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1950,
                  "sex": 2,
                  "age": 85,
                  "people": 242798
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1950,
                  "sex": 2,
                  "age": 90,
                  "people": 90766
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1960,
                  "sex": 1,
                  "age": 0,
                  "people": 10374975
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1960,
                  "sex": 1,
                  "age": 5,
                  "people": 9495503
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1960,
                  "sex": 1,
                  "age": 10,
                  "people": 8563700
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1960,
                  "sex": 1,
                  "age": 15,
                  "people": 6620902
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1960,
                  "sex": 1,
                  "age": 20,
                  "people": 5268384
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1960,
                  "sex": 1,
                  "age": 25,
                  "people": 5311805
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1960,
                  "sex": 1,
                  "age": 30,
                  "people": 5801342
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1960,
                  "sex": 1,
                  "age": 35,
                  "people": 6063063
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1960,
                  "sex": 1,
                  "age": 40,
                  "people": 5657943
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1960,
                  "sex": 1,
                  "age": 45,
                  "people": 5345658
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1960,
                  "sex": 1,
                  "age": 50,
                  "people": 4763364
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1960,
                  "sex": 1,
                  "age": 55,
                  "people": 4170581
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1960,
                  "sex": 1,
                  "age": 60,
                  "people": 3405293
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1960,
                  "sex": 1,
                  "age": 65,
                  "people": 2859371
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1960,
                  "sex": 1,
                  "age": 70,
                  "people": 2115763
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1960,
                  "sex": 1,
                  "age": 75,
                  "people": 1308913
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1960,
                  "sex": 1,
                  "age": 80,
                  "people": 619923
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1960,
                  "sex": 1,
                  "age": 85,
                  "people": 253245
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1960,
                  "sex": 1,
                  "age": 90,
                  "people": 75908
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1960,
                  "sex": 2,
                  "age": 0,
                  "people": 10146999
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1960,
                  "sex": 2,
                  "age": 5,
                  "people": 9250741
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1960,
                  "sex": 2,
                  "age": 10,
                  "people": 8310764
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1960,
                  "sex": 2,
                  "age": 15,
                  "people": 6617493
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1960,
                  "sex": 2,
                  "age": 20,
                  "people": 5513495
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1960,
                  "sex": 2,
                  "age": 25,
                  "people": 5548259
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1960,
                  "sex": 2,
                  "age": 30,
                  "people": 6090862
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1960,
                  "sex": 2,
                  "age": 35,
                  "people": 6431337
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1960,
                  "sex": 2,
                  "age": 40,
                  "people": 5940520
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1960,
                  "sex": 2,
                  "age": 45,
                  "people": 5516028
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1960,
                  "sex": 2,
                  "age": 50,
                  "people": 4928844
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1960,
                  "sex": 2,
                  "age": 55,
                  "people": 4402878
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1960,
                  "sex": 2,
                  "age": 60,
                  "people": 3723839
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1960,
                  "sex": 2,
                  "age": 65,
                  "people": 3268699
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1960,
                  "sex": 2,
                  "age": 70,
                  "people": 2516479
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1960,
                  "sex": 2,
                  "age": 75,
                  "people": 1641371
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1960,
                  "sex": 2,
                  "age": 80,
                  "people": 856952
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1960,
                  "sex": 2,
                  "age": 85,
                  "people": 384572
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1960,
                  "sex": 2,
                  "age": 90,
                  "people": 135774
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1970,
                  "sex": 1,
                  "age": 0,
                  "people": 8685121
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1970,
                  "sex": 1,
                  "age": 5,
                  "people": 10411131
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1970,
                  "sex": 1,
                  "age": 10,
                  "people": 10756403
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1970,
                  "sex": 1,
                  "age": 15,
                  "people": 9605399
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1970,
                  "sex": 1,
                  "age": 20,
                  "people": 7729202
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1970,
                  "sex": 1,
                  "age": 25,
                  "people": 6539301
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1970,
                  "sex": 1,
                  "age": 30,
                  "people": 5519879
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1970,
                  "sex": 1,
                  "age": 35,
                  "people": 5396732
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1970,
                  "sex": 1,
                  "age": 40,
                  "people": 5718538
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1970,
                  "sex": 1,
                  "age": 45,
                  "people": 5794120
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1970,
                  "sex": 1,
                  "age": 50,
                  "people": 5298312
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1970,
                  "sex": 1,
                  "age": 55,
                  "people": 4762911
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1970,
                  "sex": 1,
                  "age": 60,
                  "people": 4037643
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1970,
                  "sex": 1,
                  "age": 65,
                  "people": 3142606
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1970,
                  "sex": 1,
                  "age": 70,
                  "people": 2340826
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1970,
                  "sex": 1,
                  "age": 75,
                  "people": 1599269
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1970,
                  "sex": 1,
                  "age": 80,
                  "people": 886155
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1970,
                  "sex": 1,
                  "age": 85,
                  "people": 371123
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1970,
                  "sex": 1,
                  "age": 90,
                  "people": 186502
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1970,
                  "sex": 2,
                  "age": 0,
                  "people": 8326887
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1970,
                  "sex": 2,
                  "age": 5,
                  "people": 10003293
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1970,
                  "sex": 2,
                  "age": 10,
                  "people": 10343538
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1970,
                  "sex": 2,
                  "age": 15,
                  "people": 9414284
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1970,
                  "sex": 2,
                  "age": 20,
                  "people": 8341830
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1970,
                  "sex": 2,
                  "age": 25,
                  "people": 6903041
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1970,
                  "sex": 2,
                  "age": 30,
                  "people": 5851441
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1970,
                  "sex": 2,
                  "age": 35,
                  "people": 5708021
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1970,
                  "sex": 2,
                  "age": 40,
                  "people": 6129319
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1970,
                  "sex": 2,
                  "age": 45,
                  "people": 6198742
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1970,
                  "sex": 2,
                  "age": 50,
                  "people": 5783817
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1970,
                  "sex": 2,
                  "age": 55,
                  "people": 5222164
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1970,
                  "sex": 2,
                  "age": 60,
                  "people": 4577251
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1970,
                  "sex": 2,
                  "age": 65,
                  "people": 3894827
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1970,
                  "sex": 2,
                  "age": 70,
                  "people": 3138009
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1970,
                  "sex": 2,
                  "age": 75,
                  "people": 2293376
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1970,
                  "sex": 2,
                  "age": 80,
                  "people": 1417553
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1970,
                  "sex": 2,
                  "age": 85,
                  "people": 658511
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1970,
                  "sex": 2,
                  "age": 90,
                  "people": 314929
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1980,
                  "sex": 1,
                  "age": 0,
                  "people": 8439366
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1980,
                  "sex": 1,
                  "age": 5,
                  "people": 8680730
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1980,
                  "sex": 1,
                  "age": 10,
                  "people": 9452338
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1980,
                  "sex": 1,
                  "age": 15,
                  "people": 10698856
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1980,
                  "sex": 1,
                  "age": 20,
                  "people": 10486776
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1980,
                  "sex": 1,
                  "age": 25,
                  "people": 9624053
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1980,
                  "sex": 1,
                  "age": 30,
                  "people": 8705835
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1980,
                  "sex": 1,
                  "age": 35,
                  "people": 6852069
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1980,
                  "sex": 1,
                  "age": 40,
                  "people": 5692148
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1980,
                  "sex": 1,
                  "age": 45,
                  "people": 5342469
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1980,
                  "sex": 1,
                  "age": 50,
                  "people": 5603709
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1980,
                  "sex": 1,
                  "age": 55,
                  "people": 5485098
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1980,
                  "sex": 1,
                  "age": 60,
                  "people": 4696140
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1980,
                  "sex": 1,
                  "age": 65,
                  "people": 3893510
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1980,
                  "sex": 1,
                  "age": 70,
                  "people": 2857774
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1980,
                  "sex": 1,
                  "age": 75,
                  "people": 1840438
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1980,
                  "sex": 1,
                  "age": 80,
                  "people": 1012886
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1980,
                  "sex": 1,
                  "age": 85,
                  "people": 472338
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1980,
                  "sex": 1,
                  "age": 90,
                  "people": 204148
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1980,
                  "sex": 2,
                  "age": 0,
                  "people": 8081854
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1980,
                  "sex": 2,
                  "age": 5,
                  "people": 8275881
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1980,
                  "sex": 2,
                  "age": 10,
                  "people": 9048483
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1980,
                  "sex": 2,
                  "age": 15,
                  "people": 10410271
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1980,
                  "sex": 2,
                  "age": 20,
                  "people": 10614947
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1980,
                  "sex": 2,
                  "age": 25,
                  "people": 9827903
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1980,
                  "sex": 2,
                  "age": 30,
                  "people": 8955225
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1980,
                  "sex": 2,
                  "age": 35,
                  "people": 7134239
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1980,
                  "sex": 2,
                  "age": 40,
                  "people": 5953910
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1980,
                  "sex": 2,
                  "age": 45,
                  "people": 5697543
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1980,
                  "sex": 2,
                  "age": 50,
                  "people": 6110117
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1980,
                  "sex": 2,
                  "age": 55,
                  "people": 6160229
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1980,
                  "sex": 2,
                  "age": 60,
                  "people": 5456885
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1980,
                  "sex": 2,
                  "age": 65,
                  "people": 4896947
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1980,
                  "sex": 2,
                  "age": 70,
                  "people": 3963441
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1980,
                  "sex": 2,
                  "age": 75,
                  "people": 2951759
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1980,
                  "sex": 2,
                  "age": 80,
                  "people": 1919292
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1980,
                  "sex": 2,
                  "age": 85,
                  "people": 1023115
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1980,
                  "sex": 2,
                  "age": 90,
                  "people": 499046
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1990,
                  "sex": 1,
                  "age": 0,
                  "people": 9307465
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1990,
                  "sex": 1,
                  "age": 5,
                  "people": 9274732
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1990,
                  "sex": 1,
                  "age": 10,
                  "people": 8782542
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1990,
                  "sex": 1,
                  "age": 15,
                  "people": 9020572
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1990,
                  "sex": 1,
                  "age": 20,
                  "people": 9436188
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1990,
                  "sex": 1,
                  "age": 25,
                  "people": 10658027
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1990,
                  "sex": 1,
                  "age": 30,
                  "people": 11028712
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1990,
                  "sex": 1,
                  "age": 35,
                  "people": 9853933
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1990,
                  "sex": 1,
                  "age": 40,
                  "people": 8712632
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1990,
                  "sex": 1,
                  "age": 45,
                  "people": 6848082
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1990,
                  "sex": 1,
                  "age": 50,
                  "people": 5553992
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1990,
                  "sex": 1,
                  "age": 55,
                  "people": 4981670
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1990,
                  "sex": 1,
                  "age": 60,
                  "people": 4953822
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1990,
                  "sex": 1,
                  "age": 65,
                  "people": 4538398
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1990,
                  "sex": 1,
                  "age": 70,
                  "people": 3429420
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1990,
                  "sex": 1,
                  "age": 75,
                  "people": 2344932
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1990,
                  "sex": 1,
                  "age": 80,
                  "people": 1342996
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1990,
                  "sex": 1,
                  "age": 85,
                  "people": 588790
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1990,
                  "sex": 1,
                  "age": 90,
                  "people": 238459
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1990,
                  "sex": 2,
                  "age": 0,
                  "people": 8894007
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1990,
                  "sex": 2,
                  "age": 5,
                  "people": 8799955
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1990,
                  "sex": 2,
                  "age": 10,
                  "people": 8337284
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1990,
                  "sex": 2,
                  "age": 15,
                  "people": 8590991
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1990,
                  "sex": 2,
                  "age": 20,
                  "people": 9152644
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1990,
                  "sex": 2,
                  "age": 25,
                  "people": 10587292
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1990,
                  "sex": 2,
                  "age": 30,
                  "people": 11105750
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1990,
                  "sex": 2,
                  "age": 35,
                  "people": 10038644
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1990,
                  "sex": 2,
                  "age": 40,
                  "people": 8928252
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1990,
                  "sex": 2,
                  "age": 45,
                  "people": 7115129
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1990,
                  "sex": 2,
                  "age": 50,
                  "people": 5899925
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1990,
                  "sex": 2,
                  "age": 55,
                  "people": 5460506
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1990,
                  "sex": 2,
                  "age": 60,
                  "people": 5663205
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1990,
                  "sex": 2,
                  "age": 65,
                  "people": 5594108
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1990,
                  "sex": 2,
                  "age": 70,
                  "people": 4610222
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1990,
                  "sex": 2,
                  "age": 75,
                  "people": 3723980
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1990,
                  "sex": 2,
                  "age": 80,
                  "people": 2545730
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1990,
                  "sex": 2,
                  "age": 85,
                  "people": 1419494
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 1990,
                  "sex": 2,
                  "age": 90,
                  "people": 745146
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 2000,
                  "sex": 1,
                  "age": 0,
                  "people": 9735380
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 2000,
                  "sex": 1,
                  "age": 5,
                  "people": 10552146
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 2000,
                  "sex": 1,
                  "age": 10,
                  "people": 10563233
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 2000,
                  "sex": 1,
                  "age": 15,
                  "people": 10237419
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 2000,
                  "sex": 1,
                  "age": 20,
                  "people": 9731315
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 2000,
                  "sex": 1,
                  "age": 25,
                  "people": 9659493
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 2000,
                  "sex": 1,
                  "age": 30,
                  "people": 10205879
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 2000,
                  "sex": 1,
                  "age": 35,
                  "people": 11475182
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 2000,
                  "sex": 1,
                  "age": 40,
                  "people": 11320252
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 2000,
                  "sex": 1,
                  "age": 45,
                  "people": 9925006
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 2000,
                  "sex": 1,
                  "age": 50,
                  "people": 8507934
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 2000,
                  "sex": 1,
                  "age": 55,
                  "people": 6459082
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 2000,
                  "sex": 1,
                  "age": 60,
                  "people": 5123399
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 2000,
                  "sex": 1,
                  "age": 65,
                  "people": 4453623
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 2000,
                  "sex": 1,
                  "age": 70,
                  "people": 3792145
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 2000,
                  "sex": 1,
                  "age": 75,
                  "people": 2912655
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 2000,
                  "sex": 1,
                  "age": 80,
                  "people": 1902638
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 2000,
                  "sex": 1,
                  "age": 85,
                  "people": 970357
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 2000,
                  "sex": 1,
                  "age": 90,
                  "people": 336303
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 2000,
                  "sex": 2,
                  "age": 0,
                  "people": 9310714
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 2000,
                  "sex": 2,
                  "age": 5,
                  "people": 10069564
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 2000,
                  "sex": 2,
                  "age": 10,
                  "people": 10022524
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 2000,
                  "sex": 2,
                  "age": 15,
                  "people": 9692669
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 2000,
                  "sex": 2,
                  "age": 20,
                  "people": 9324244
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 2000,
                  "sex": 2,
                  "age": 25,
                  "people": 9518507
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 2000,
                  "sex": 2,
                  "age": 30,
                  "people": 10119296
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 2000,
                  "sex": 2,
                  "age": 35,
                  "people": 11635647
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 2000,
                  "sex": 2,
                  "age": 40,
                  "people": 11488578
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 2000,
                  "sex": 2,
                  "age": 45,
                  "people": 10261253
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 2000,
                  "sex": 2,
                  "age": 50,
                  "people": 8911133
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 2000,
                  "sex": 2,
                  "age": 55,
                  "people": 6921268
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 2000,
                  "sex": 2,
                  "age": 60,
                  "people": 5668961
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 2000,
                  "sex": 2,
                  "age": 65,
                  "people": 4804784
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 2000,
                  "sex": 2,
                  "age": 70,
                  "people": 5184855
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 2000,
                  "sex": 2,
                  "age": 75,
                  "people": 4355644
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 2000,
                  "sex": 2,
                  "age": 80,
                  "people": 3221898
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 2000,
                  "sex": 2,
                  "age": 85,
                  "people": 1981156
                },
                "doc_count": 1
              },
              {
                "key": {
                  "year": 2000,
                  "sex": 2,
                  "age": 90,
                  "people": 1064581
                },
                "doc_count": 1
              }
            ]
          }
        }
      }
    },
    {
      "name": "popYear",
      "source": "population",
      "transform": [
        {
          "type": "filter",
          "expr": "datum.key.year == year"
        }
      ]
    },
    {
      "name": "males",
      "source": "popYear",
      "transform": [
        {
          "type": "filter",
          "expr": "datum.key.sex == 1"
        }
      ]
    },
    {
      "name": "females",
      "source": "popYear",
      "transform": [
        {
          "type": "filter",
          "expr": "datum.key.sex == 2"
        }
      ]
    },
    {
      "name": "ageGroups",
      "source": "population",
      "transform": [
        {
          "type": "aggregate",
          "groupby": [
            "age"
          ]
        }
      ]
    }
  ],
  "transform": [
    {
      "calculate": "datum.key.year",
      "as": "year"
    },
    {
      "calculate": "datum.key.sex",
      "as": "sex"
    },
    {
      "calculate": "datum.key.age",
      "as": "age"
    },
    {
      "calculate": "datum.key.people",
      "as": "people"
    }
  ],
  "scales": [
    {
      "name": "y",
      "type": "band",
      "range": [
        {
          "signal": "height"
        },
        0
      ],
      "round": true,
      "domain": {
        "data": "population",
        "field": "key.age"
      }
    },
    {
      "name": "c",
      "type": "ordinal",
      "domain": [
        1,
        2
      ],
      "range": [
        "#d5855a",
        "#6c4e97"
      ]
    }
  ],
  "marks": [
    {
      "type": "text",
      "interactive": false,
      "from": {
        "data": "population"
      },
      "encode": {
        "enter": {
          "x": {
            "signal": "chartWidth + chartPad / 2"
          },
          "y": {
            "scale": "y",
            "field": "key.age",
            "band": 0.5
          },
          "text": {
            "field": "key.age"
          },
          "baseline": {
            "value": "middle"
          },
          "align": {
            "value": "center"
          },
          "fill": {
            "value": "#000"
          }
        }
      }
    },
    {
      "type": "group",
      "encode": {
        "update": {
          "x": {
            "value": 0
          },
          "height": {
            "signal": "height"
          }
        }
      },
      "scales": [
        {
          "name": "x",
          "type": "linear",
          "range": [
            {
              "signal": "chartWidth"
            },
            0
          ],
          "nice": true,
          "zero": true,
          "domain": {
            "data": "population",
            "field": "key.people"
          }
        }
      ],
      "axes": [
        {
          "orient": "bottom",
          "scale": "x",
          "format": "s",
          "title": "Females"
        }
      ],
      "marks": [
        {
          "type": "rect",
          "from": {
            "data": "females"
          },
          "encode": {
            "enter": {
              "x": {
                "scale": "x",
                "field": "key.people"
              },
              "x2": {
                "scale": "x",
                "value": 0
              },
              "y": {
                "scale": "y",
                "field": "key.age"
              },
              "height": {
                "scale": "y",
                "band": 1,
                "offset": -1
              },
              "fillOpacity": {
                "value": 0.6
              },
              "fill": {
                "scale": "c",
                "field": "key.sex"
              }
            }
          }
        }
      ]
    },
    {
      "type": "group",
      "encode": {
        "update": {
          "x": {
            "signal": "chartWidth + chartPad"
          },
          "height": {
            "signal": "height"
          }
        }
      },
      "scales": [
        {
          "name": "x",
          "type": "linear",
          "range": [
            0,
            {
              "signal": "chartWidth"
            }
          ],
          "nice": true,
          "zero": true,
          "domain": {
            "data": "population",
            "field": "key.people"
          }
        }
      ],
      "axes": [
        {
          "orient": "bottom",
          "scale": "x",
          "format": "s",
          "title": "Males"
        }
      ],
      "marks": [
        {
          "type": "rect",
          "from": {
            "data": "males"
          },
          "encode": {
            "enter": {
              "x": {
                "scale": "x",
                "field": "key.people"
              },
              "x2": {
                "scale": "x",
                "value": 0
              },
              "y": {
                "scale": "y",
                "field": "key.age"
              },
              "height": {
                "scale": "y",
                "band": 1,
                "offset": -1
              },
              "fillOpacity": {
                "value": 0.6
              },
              "fill": {
                "scale": "c",
                "field": "key.sex"
              }
            }
          }
        }
      ]
    }
  ],
  "config": {
    "range": {
      "category": {
        "scheme": "elastic"
      }
    },
    "arc": {
      "fill": "#54B399"
    },
    "area": {
      "fill": "#54B399"
    },
    "line": {
      "stroke": "#54B399"
    },
    "path": {
      "stroke": "#54B399"
    },
    "rect": {
      "fill": "#54B399"
    },
    "rule": {
      "stroke": "#54B399"
    },
    "shape": {
      "stroke": "#54B399"
    },
    "symbol": {
      "fill": "#54B399"
    },
    "trail": {
      "fill": "#54B399"
    },
    "title": {
      "color": "#343741"
    },
    "style": {
      "guide-label": {
        "fill": "#69707d"
      },
      "guide-title": {
        "fill": "#343741"
      },
      "group-title": {
        "fill": "#343741"
      },
      "group-subtitle": {
        "fill": "#343741"
      }
    },
    "axis": {
      "tickColor": "#eef0f3",
      "domainColor": "#eef0f3",
      "gridColor": "#eef0f3"
    },
    "background": "transparent"
  },
  "width": "container",
  "autosize": {
    "type": "fit",
    "contains": "padding"
  }
}
