import os
import sys
import time
import json

from mongoengine import Q

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from models.case_3 import BaseCase


if __name__ == '__main__':
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

    pipe = {
        "$set": {
            "d.y": "update from aggregate"
        }
    }
    t = time.time()  
    obj = BaseCase._get_collection().update_many({},[pipe])
    print(f"bulk update using aggregate: {time.time() - t}")
    
    breakpoint()
