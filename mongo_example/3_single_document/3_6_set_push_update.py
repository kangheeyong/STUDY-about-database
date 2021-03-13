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
    1.
        data setting time: 4.44744610786438
        bulk update at mongoengine case 1: 3.0211143493652344
        bulk update at mongoengine case 2: 7.057666778564453
    2.
        data setting time: 4.455876111984253
        bulk update using pymongo case 1: 0.00171065330505371
        bulk update using pymongo case 2: 0.02818751335144043

    case1 약 3000배 성능 향상
    case2 약 250배 성능 향상
    """
    t = time.time()
    BaseCase.make_dataset()
    print(f"data setting time: {time.time() - t}")

    for obj in BaseCase.objects:
        assert len(obj.g) == 1000

    #######################################################

    # t = time.time()
    # for obj in BaseCase.objects:
    #     if "13" not in obj.g:
    #         obj.g.append("13")
    #         obj.save()
    # print(f"bulk update at mongoengine case 1: {time.time() - t}")

    # for obj in BaseCase.objects:
    #     assert len(obj.g) == 1000

    # t = time.time()
    # for obj in BaseCase.objects:
    #     if "1000" not in obj.g:
    #         obj.g.append("1000")
    #         obj.save()
    # print(f"bulk update at mongoengine case 2: {time.time() - t}")

    # for obj in BaseCase.objects:
    #     assert len(obj.g) == 1001

    #######################################################

    t = time.time()
    _filter = {}
    _update = {"$addToSet": {"g": "13"}}
    obj = BaseCase._get_collection().update_one(_filter, _update)
    print(f"bulk update using pymongo case 1: {time.time() - t}")
    for obj in BaseCase.objects:
        assert len(obj.g) == 1000

    t = time.time()
    _filter = {}
    _update = {"$addToSet": {"g": "1000"}}
    obj = BaseCase._get_collection().update_many(_filter, _update)
    print(f"bulk update using pymongo case 2: {time.time() - t}")
    for obj in BaseCase.objects:
        assert len(obj.g) == 1001

    breakpoint()
