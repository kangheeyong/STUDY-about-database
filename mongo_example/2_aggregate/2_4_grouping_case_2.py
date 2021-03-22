import os
import sys
import time
from datetime import datetime
from collections import defaultdict

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from models.case_4 import BaseCase


if __name__ == "__main__":
    """
    BaseCase.make_dataset_mongoengine() 에서 업데이트 하는 방식을
    순수 몽고 명령어로 못짜겠다...
    """
    t = time.time()
    BaseCase.objects.delete()
    print(f"delete dataset {time.time() - t}")

    ########################################################

    # t = time.time()
    # BaseCase.make_dataset_mongoengine()
    # print(f"case4 update case python {time.time() - t}")
    # t = time.time()
    # key_meta = defaultdict(dict)
    # objs = BaseCase.objects(a__gte='a-000', a__lte='a-005')
    # for obj in objs:
    #     for o in obj.d:
    #         if o.grouping_key in key_meta:
    #             key_meta[o.grouping_key]["count"] += o.cnt
    #         else:
    #             key_meta[o.grouping_key] = {
    #                 "z": o.z, "y": o.y, "x": o.x, "count": o.cnt, "key": o.grouping_key
    #             }
    # result = sorted(key_meta.values(), key=lambda x: (-x["count"], x["key"]))
    # print(f"case4 get case python {time.time() - t}")


    ########################################################
    BaseCase.make_dataset_mongoengine_v2()
    # t = time.time()
    # _unwind = { "$unwind" : "$d" }
    # _group = {
    #     "$group": {
    #         "_id": "$d.grouping_key",
    #         "count": {"$sum": "$d.cnt"},
    #         "meta": {"$last": "$d"}
    #     }
    # }
    # _sort = {
    #     "$sort": {"count": -1, "_id": 1}
    # }

    # result1 = list(
    #     BaseCase.objects(
    #         a__gte='a-000', a__lte='a-005'
    #     ).aggregate([_unwind, _group, _sort])
    # )
    # print(f"case2 grouping {time.time() - t}")
    
    breakpoint()
