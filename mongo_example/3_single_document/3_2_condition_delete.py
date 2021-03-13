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
    data setting time: 3.987682580947876
    bulk update at mongoengine: 6.604163885116577
    bulk update using aggregate: 0.028783321380615234
    약 280배 속도 향상
    """
    t = time.time()
    BaseCase.make_dataset()
    print(f"data setting time: {time.time() - t}")

    t = time.time()
    for obj in BaseCase.objects:
        for idx in range(len(obj.d) - 1, -1, -1):
            if "5-5" in obj.d[idx].y:
                del obj.d[idx]
        obj.save()
    print(f"bulk update at mongoengine: {time.time() - t}")

    #######################################################

    pipe_match = {}
    pipe_set = {"$pull": {"d": {"y": re.compile("4-5", re.IGNORECASE)}}}

    t = time.time()
    # arrayFilter를 쓸 경우 pipe_set에는 반드시 dict로 해야한다
    # 아마도 하나의 set만 가능한 것 같다
    obj = BaseCase._get_collection().update_many(pipe_match, pipe_set)
    print(f"bulk update using aggregate: {time.time() - t}")

    breakpoint()
