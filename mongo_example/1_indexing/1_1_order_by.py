import os
import sys
import json
import time
from random import randint

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from models.case_1 import Case1, Case5


if __name__ == "__main__":
    """
    data setting time: 13.09441065788269
    Case5 result: 8.487701416015625e-05
    Case1 result: 8.392333984375e-05
    """
    t = time.time()
    Case5.make_dateset()
    Case1.make_dateset()
    print(f"data setting time: {time.time() - t}")

    objs1, objs5 = [], []
    l = len(Case5.objects)
    for _ in range(500):
        objs5.append(Case5.objects[randint(0, l)].id)
    for _ in range(500):
        objs1.append(Case1.objects[randint(0, l)].id)

    data0 = Case5.objects.filter(id__in=objs5[:20]).explain()
    data1 = Case5.objects.filter(id__in=objs5[:20]).order_by("a").explain()
    data2 = Case5.objects.filter(id__in=objs5[:20]).order_by("a").limit(5).explain()

    t = time.time()
    obj = Case5.objects.filter(id__in=objs5).order_by("a").limit(100)
    print(f"Case5 result: {time.time() - t}")

    data3 = Case1.objects.filter(id__in=objs1[:20]).explain()
    data4 = Case1.objects.filter(id__in=objs1[:20]).order_by("a").explain()
    data5 = Case1.objects.filter(id__in=objs1[:20]).order_by("a").limit(5).explain()

    t = time.time()
    obj = Case1.objects.filter(id__in=objs1).order_by("a").limit(100)
    print(f"Case1 result: {time.time() - t}")
