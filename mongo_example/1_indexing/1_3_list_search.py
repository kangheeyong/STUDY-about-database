import os
import sys
import json
import time
from random import randint

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from models.case_1 import Case1, Case7, Case7_1


if __name__ == "__main__":
    """
    https://docs.mongodb.com/manual/tutorial/query-array-of-documents/

    data setting time: 216.50885486602783
    Case7_1 result: 0.008502483367919922
    Case7 result: 0.13920116424560547
    Case1 result: 0.13925790786743164

    약 15배 성능 향상
    case7_1 인덱싱 검색
    case7 인덱싱 사용 x why? -> https://docs.mongodb.com/manual/core/index-partial/
    """
    t = time.time()
    Case7_1.make_dateset_v7()
    Case7.make_dateset_v7()
    Case1.make_dateset_v7()
    print(f"data setting time: {time.time() - t}")

    t = time.time()
    obj7_1 = list(Case7_1.objects.filter(d__match={"z": "e-50", "y": "e-50"}))
    print(f"Case7_1 result: {time.time() - t}")

    r7_1 = Case7_1.objects.filter(d__match={"z": "e-50", "y": "e-50"}).explain()

    t = time.time()
    obj7 = list(
        Case7.objects.filter(
            d__match={
                "z": {"$type": "string", "$eq": "e-50"},
                "y": {"$type": "string", "$eq": "e-50"},
            }
        )
    )
    print(f"Case7 result: {time.time() - t}")

    r7 = Case7.objects.filter(
        d__match={
            "z": {"$type": "string", "$eq": "e-50"},
            "y": {"$type": "string", "$eq": "e-50"},
        }
    ).explain()

    t = time.time()
    obj1 = list(Case1.objects.filter(d__match={"z": "e-50", "y": "e-50"}))
    print(f"Case1 result: {time.time() - t}")

    r1 = Case1.objects.filter(d__match={"z": "e-50", "y": "e-50"}).explain()

    # _match = {
    #     "$match": {
    #         "d": {"$elemMatch": {"z": "e-50", "y": "e-50"}}
    #     }
    # }
    # t = time.time()
    # r = list(Case7._get_collection().aggregate([_match]))
    # print(f"Case7 aggregate result: {time.time() - t}")

    # t = time.time()
    # r1 = list(
    #     Case7._get_collection().find(
    #         {"d": {"$elemMatch": {"z": "e-50", "y": "e-50"}}}
    #     )
    # )
    # print(f"Case7 search result with elemMatch: {time.time() - t}")
    # assert len(r1) == 1

    # t = time.time()
    # r2 = list(
    #     Case7._get_collection().find(
    #         {"d": {"z": "e-50", "y": "e-50"}}
    #     )
    # )
    # print(f"Case7 search result: {time.time() - t}")
    # assert len(r2) != 1

    breakpoint()
