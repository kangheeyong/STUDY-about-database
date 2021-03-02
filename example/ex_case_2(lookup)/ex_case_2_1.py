import os
import sys
import time
import json

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from models.case_2 import make_dateset, Case1_1, Case1_2


if __name__ == "__main__":
    make_dateset(Case1_1, Case1_2)

    t = time.time()
    objs1 = list(Case1_2.objects)
    print(f"case1 {time.time() - t}")

    t = time.time()
    objs2 =[]
    for obj in Case1_2.objects:
        objs2.append(obj)
    print(f"case2 {time.time() - t}")

    pipe = {
        "$lookup": {
            "from": Case1_1._get_collection_name(),
            "localField": "d",
            "foreignField": "_id",
            "as": "new"
        }
    }
    pipe1 = {
        "$project":{
            "_id": 1,
            "c": 1,
            "new.a":1,
            "new.b":1
        }
    }
    t = time.time()
    objs3 = list(Case1_2.objects.aggregate([pipe]))
    print(f"case3(aggregate) {time.time() - t}")

    t = time.time()
    objs4 = list(Case1_2.objects.aggregate([pipe, pipe1]))
    print(f"case4(aggregate1) {time.time() - t}")
    
    t = time.time()
    objs5=[]
    for obj in Case1_2.objects:
        objs5.append(obj.d.fetch())
    print(f"python {time.time() - t}")
    #objs = Case1_2.objects.aggregate(*pipe)
    breakpoint()
    print("end")
