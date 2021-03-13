import os
import sys
import time
import json

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from models.case_2 import make_dateset, Case1_1, Case1_2


if __name__ == "__main__":
    '''
    make dataset 14.393730640411377
    case1(aggregate) 0.804481983184814
    case2(aggregate) 0.8415446281433105
    case1(python) 8.060422658920288
    '''
    t = time.time()
    make_dateset(Case1_1, Case1_2)
    print(f"make dataset {time.time() - t}")

#######################################################

    _lookup = {
        "$lookup": {
            "from": Case1_1._get_collection_name(),
            "localField": "d",
            "foreignField": "_id",
            "as": "new"
        }
    }

    t = time.time()
    objs1 = list(Case1_2.objects.aggregate([_lookup]))
    print(f"case1(aggregate) {time.time() - t}")

#######################################################

    t = time.time()
    objs2 = list(Case1_2._get_collection().aggregate([_lookup]))
    print(f"case2(aggregate) {time.time() - t}")

#######################################################

    t = time.time()
    objs3=[]
    for obj in Case1_2.objects:
        objs3.append(obj.d.fetch())
    print(f"case1(python) {time.time() - t}")

    breakpoint()
