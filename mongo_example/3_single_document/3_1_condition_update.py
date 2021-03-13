import os
import re
import sys
import time
import json

from mongoengine import Q

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from models.case_3 import BaseCase


if __name__ == "__main__":
    """
    data setting time: 4.288562774658203
    bulk update at mongoengine: 11.433610439300537
    bulk update using aggregate: 0.027959823608398438
    약 500배 속도 향상
    """
    t = time.time()
    BaseCase.make_dataset()
    print(f"data setting time: {time.time() - t}")

    t = time.time()
    for obj in BaseCase.objects:
        for o in obj.d:
            if o.y == "5-5-y":
                o.y = "edited"
        obj.save()
    print(f"bulk update at mongoengine: {time.time() - t}")

    #######################################################

    pipe_match = {}
    pipe_set = {"$set": {"d.$[idx].y": "updated from cmd"}}
    array_filters = [{"idx.y": re.compile("5-5-y", re.IGNORECASE)}]

    t = time.time()
    # arrayFilter를 쓸 경우 pipe_set에는 반드시 dict로 해야한다
    # 아마도 하나의 set만 가능한 것 같다
    obj = BaseCase._get_collection().update_many(
        pipe_match, pipe_set, upsert=True, array_filters=array_filters
    )
    print(f"bulk update using aggregate: {time.time() - t}")

    breakpoint()
