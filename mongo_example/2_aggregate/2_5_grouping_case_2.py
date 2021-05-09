import os
import sys
import time
import json
from datetime import datetime
from collections import defaultdict

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from models.case_2 import make_dateset, Case1_1, Case1_2


if __name__ == "__main__":
    """
    make dataset 19.47690200805664
    case2 python 0.5037868022918701
    case2 grouping 0.017148256301879883
    약 29배 성능 향상
    """
    t = time.time()
    make_dateset(Case1_1, Case1_2)
    print(f"make dataset {time.time() - t}")

    ########################################################

    t = time.time()
    objs = Case1_2.objects
    dic = defaultdict(int)
    for obj in objs:
        if obj.b == "2-b-5" and obj.c == "2-c-5":
            dic[obj.a] += 1

    print(f"case2 python {time.time() - t}")

    ########################################################

    t = time.time()
    _group = {
        "$group": {
            "_id": "$a",
            "count": {
                "$sum": {
                    "$cond": [
                        {"$and": [{"$eq": ["$b", "2-b-5"]}, {"$eq": ["$c", "2-c-5"]}]},
                        1,
                        0,
                    ]
                }
            },
        }
    }
    _match = {"$match": {"count": {"$gt": 0}}}
    _sort = {"$sort": {"_id": 1}}
    result = list(Case1_2.objects.aggregate(_group, _match, _sort))
    print(f"case2 grouping {time.time() - t}")

    breakpoint()
