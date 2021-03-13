import os
import sys
import time
import json
from datetime import datetime
from collections import defaultdict

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from models.case_2 import make_dateset, Case1_1, Case1_2


if __name__ == "__main__":
    '''
    1. 
        make dataset 14.67024564743042
        case2(aggregate1) 0.013969659805297852
        case2(aggregate2) 0.00823354721069336
        case2(aggregate3) 0.007085561752319336
        python 0.009839296340942383
    2. 
        make dataset 15.569779634475708
        case2(aggregate1) 0.008602380752563477
        case2(aggregate2) 0.006581783294677734
        case2(aggregate3) 0.00905466079711914
        python 0.011057615280151367
    3. 
        make dataset 15.363036632537842
        case2(aggregate1) 0.007440805435180664
        case2(aggregate2) 0.007063865661621094
        case2(aggregate3) 0.009218692779541016
        python 0.012164831161499023
    query 호출 방식을 다양하게 해보았으나
    의외로 성능 차이는 없는 것 같다
    '''
    t = time.time()
    make_dateset(Case1_1, Case1_2)
    print(f"make dataset {time.time() - t}")
    
    _match = {
        "$match": {
            "$and": [
                {"b": {"$eq": "2-b-5"}},
                {"e": {"$gte": datetime(2005, 1, 1, 0, 0, 0)}},
                {"e": {"$lte": datetime(2007, 1, 1, 0, 0, 0)}}
            ]
        }
    }
    _project = {
        "$project":{
            "_id": 1,
            "a":1,
            "b":1
        }
    }

########################################################

    t = time.time()
    result = list(
        Case1_2.objects.filter(
            b="2-b-5",
            e__gte=datetime(2005, 1, 1, 0, 0, 0),
            e__lte=datetime(2007, 1, 1, 0, 0, 0)
        ).aggregate(_project)
    )
    print(f"case2(aggregate1) {time.time() - t}")

########################################################

    t = time.time()
    result1 = list(
        Case1_2.objects.aggregate(
            [
                _match,
                _project
            ]
        )
    )
    print(f"case2(aggregate2) {time.time() - t}")


########################################################

    t = time.time()
    result2 = list(
        Case1_2._get_collection().aggregate(
            [
                _match,
                _project
            ]
        )
    )
    print(f"case2(aggregate3) {time.time() - t}")

########################################################
    t = time.time()
    result3 = list(
        Case1_2.objects.filter(
            b="2-b-5",
            e__gte=datetime(2005, 1, 1, 0, 0, 0),
            e__lte=datetime(2007, 1, 1, 0, 0, 0)
        )
    )
    print(f"python {time.time() - t}")

    breakpoint()
