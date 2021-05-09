import os
import sys
import time
from datetime import datetime
from collections import defaultdict

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from models.case_4 import BaseCase


if __name__ == "__main__":
    """
    case4 get case python 0.014491796493530273
    case2 grouping 0.0017268657684326172
    약 8배 더 빠름
    """
    t = time.time()
    BaseCase.objects.delete()
    print(f"delete dataset {time.time() - t}")

    ########################################################

    t = time.time()
    BaseCase.make_dataset_mongoengine()
    print(f"case4 update case python {time.time() - t}")
    t = time.time()
    key_meta = defaultdict(dict)
    objs = BaseCase.objects
    for obj in objs:
        for o in obj.d:
            if o.grouping_key in key_meta:
                key_meta[o.grouping_key]["count"] += o.cnt
            else:
                key_meta[o.grouping_key] = {"count": o.cnt}
    result = sorted(key_meta.items(), key=lambda x: (-x[1]["count"], x[0]))
    print(f"case4 get case python {time.time() - t}")

    ########################################################
    t = time.time()
    _unwind = { "$unwind" : "$d" }
    _group = {
        "$group": {
            "_id": "$d.grouping_key",
            "count": {"$sum": "$d.cnt"}
        }
    }
    _sort = {
        "$sort": {"count": -1, "_id": 1}
    }

    result1 = list(
        BaseCase.objects.aggregate([_unwind, _group, _sort])
    )
    print(f"case2 grouping {time.time() - t}")
    
    breakpoint()
