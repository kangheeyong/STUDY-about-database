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
    data setting time: 4.014416933059692
    bulk update at mongoengine: 6.326115608215332
    bulk update using aggregate: 0.07535076141357422
    약 90배 성능 향상
    """
    t = time.time()
    BaseCase.make_dataset()
    print(f"data setting time: {time.time() - t}")

    t = time.time()
    for obj in BaseCase.objects:
        del obj.e["e_3"]
        obj.save()
    print(f"bulk update at mongoengine: {time.time() - t}")

    #######################################################

    pipe_match = {}
    pipe_set = {"$unset": "e.e_2"}

    t = time.time()
    # arrayFilter를 쓸 경우 pipe_set에는 반드시 dict로 해야한다
    # 아마도 하나의 set만 가능한 것 같다
    obj = BaseCase._get_collection().update_many(pipe_match, [pipe_set])
    print(f"bulk update using aggregate: {time.time() - t}")

    breakpoint()
