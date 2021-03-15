import os
import sys
import time
import json
from datetime import datetime
from collections import defaultdict

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from models.case_2 import make_dateset, Case1_1, Case1_2


if __name__ == "__main__":
    """
    make dataset 30.817030668258667
    case2 python 0.5368857383728027
    case2 grouping 0.02013707160949707
    약 25배 성능 향상
    """
    t = time.time()
    make_dateset(Case1_1, Case1_2)
    print(f"make dataset {time.time() - t}")

    ########################################################

    t = time.time()
    objs = Case1_2.objects
    dic = defaultdict(int)
    for obj in objs:
        dic[obj.b] += obj.f

    print(f"case2 python {time.time() - t}")

    ########################################################

    t = time.time()
    _group = {
        "$group": {
            "_id": "$b",
            "count": {"$sum": "$f"}
        }
    }
    result = list(Case1_2.objects.aggregate(_group))
    print(f"case2 grouping {time.time() - t}")
    
    breakpoint()
