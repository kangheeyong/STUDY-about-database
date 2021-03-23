import os
import sys
import json
import time
from random import randint

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from models.case_1 import Case1, Case6


if __name__ == "__main__":
    """
    array는 Multikey Indexes를 사용해야 한다
    link: https://docs.mongodb.com/manual/core/index-multikey/#multikey-indexes

    data setting time: 137.64821791648865
    Case5 result: 0.005915641784667969
    Case1 result: 0.19394373893737793
    33배 속도 향상
    """
    t = time.time()
    Case6.make_dateset_v6()
    Case1.make_dateset_v6()
    print(f"data setting time: {time.time() - t}")

    t = time.time()
    obj5 = list(Case6.objects.filter(d__z="5000"))
    print(f"Case5 result: {time.time() - t}")

    r5 = Case6.objects.filter(d__z="5000").explain()

    t = time.time()
    obj1 = list(Case1.objects.filter(d__z="5000"))
    print(f"Case1 result: {time.time() - t}")

    r1 = Case1.objects.filter(d__z="5000").explain()

    breakpoint()
