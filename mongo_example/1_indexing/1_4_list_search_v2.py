import os
import sys
import json
import time
from random import randint

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from models.case_1 import Case1, Case8, Case8_1


if __name__ == "__main__":
    """
    https://docs.mongodb.com/manual/tutorial/query-array-of-documents/
    
    data setting time: 207.41723346710205
    Case8_1 result: 0.004520893096923828
    Case8 result: 0.1414954662322998
    Case1 result: 0.1394059658050537

    약 15배 성능 향상
    case7_1 인덱싱 검색
    case7 인덱싱 사용 x why? 이유 -> https://docs.mongodb.com/manual/core/index-partial/
    """
    t = time.time()
    Case8_1.make_dateset_v8()
    Case8.make_dateset_v8()
    Case1.make_dateset_v8()
    print(f"data setting time: {time.time() - t}")

    t = time.time()
    obj8_1 = list(Case8_1.objects.filter(d__match={"z": "e-50", "y": "e-50"}))
    print(f"Case8_1 result: {time.time() - t}")

    r8_1 = Case8_1.objects.filter(d__match={"z": "e-50", "y": "e-50"}).explain()

    t = time.time()
    obj8 = list(Case8.objects.filter(d__match={"z": {"$type": "string", "$eq": "e-50"}, "y": {"$type": "string", "$eq": "e-50"}}))
    print(f"Case8 result: {time.time() - t}")

    r8 = Case8.objects.filter(d__match={"z": {"$type": "string", "$eq": "e-50"}, "y": {"$type": "string", "$eq": "e-50"}}).explain()

    t = time.time()
    obj1 = list(Case1.objects.filter(d__match={"z": "e-50", "y": "e-50"}))
    print(f"Case1 result: {time.time() - t}")

    r1 = Case1.objects.filter(d__match={"z": "e-50", "y": "e-50"}).explain()

    breakpoint()
