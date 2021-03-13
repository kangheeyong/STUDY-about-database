import os
import sys
import time
import json

from mongoengine import Q

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from models.case_3 import BaseCase


if __name__ == "__main__":
    """
    data setting time: 4.423297166824341
    bulk update at mongoengine: 416.9906141757965
    bulk update using aggregate: 0.08883404731750488
    약 5000배 속도 향상
    """
    t = time.time()
    BaseCase.make_dataset()
    print(f"data setting time: {time.time() - t}")

    t = time.time()
    for obj in BaseCase.objects:
        for o in obj.d:
            o.y = "edited"
        obj.save()
    print(f"bulk update at mongoengine: {time.time() - t}")

    #######################################################

    pipe = {"$set": {"d.y": "update from aggregate"}}
    t = time.time()
    obj = BaseCase._get_collection().update_many({}, [pipe])
    print(f"bulk update using aggregate: {time.time() - t}")

    breakpoint()
