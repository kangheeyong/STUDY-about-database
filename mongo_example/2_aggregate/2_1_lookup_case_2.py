import os
import sys
import time
import json
from collections import defaultdict

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from models.case_2 import make_dateset, Case1_1, Case1_2


if __name__ == "__main__":
    '''
    make dataset 14.642764806747437
    case1(aggregate1) 0.816481351852417
    case2(aggregate2) 0.8156464099884033
    python 8.205116987228394
    '''
    t = time.time()
    make_dateset(Case1_1, Case1_2)
    print(f"make dataset {time.time() - t}")

########################################################

    _lookup = {
        "$lookup": {
            "from": Case1_1._get_collection_name(),
            "localField": "d",
            "foreignField": "_id",
            "as": "new"
        }
    }
    _project = {
        "$project":{
            "_id": 1,
            "c": 1,
            "new.a":1,
            "new.b":1
        }
    }

    t = time.time()
    objs1 = list(Case1_2.objects.aggregate([_lookup, _project]))
    print(f"case1(aggregate1) {time.time() - t}")

########################################################

    t = time.time()
    objs2 = list(Case1_2._get_collection().aggregate([_lookup, _project]))
    print(f"case2(aggregate2) {time.time() - t}")

  ########################################################

    t = time.time()
    objs = []
    for obj in Case1_2.objects:
        objs.append(
            {
                "_id": obj.id,
                "c": obj.c,
                "new": {
                    "a": obj.d.fetch().a,
                    "b": obj.d.fetch().b
                }
            }
        )
        
    print(f"python {time.time() - t}")
    breakpoint()
