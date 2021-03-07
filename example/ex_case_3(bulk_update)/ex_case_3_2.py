import os
import re
import sys
import time
import json

from mongoengine import Q

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from models.case_3 import BaseCase


if __name__ == '__main__':
    '''
    아래와 같이 $unset으로 list 내에 있는 embeded document를 지우면
    그 필드가 실제 db에 null로 치환이 되고, 이에 따라서 mongoengine에서
    데이터를 읽어 올 때 에러가 걸린다

    TODO: null로 치환이 안되게 하는 방법을 찾아보자!!
    '''
    t = time.time()    
    BaseCase.make_dataset()
    print(f"data setting time: {time.time() - t}")

    # t = time.time()    
    # for obj in BaseCase.objects:
    #     for o in obj.d:
    #         if o.y == '5-5-y':
    #             o.y = "edited"
    #     obj.save()
    # print(f"bulk update at mongoengine: {time.time() - t}")

    #######################################################

    pipe_match = {}
    pipe_set = {
        "$unset": {
            "d.$[idx]": 1
        }
    }
    array_filters = [
        {"idx.y": re.compile('5-5-y', re.IGNORECASE)}
    ]

    t = time.time()
    # arrayFilter를 쓸 경우 pipe_set에는 반드시 dict로 해야한다
    # 아마도 하나의 set만 가능한 것 같다
    obj = BaseCase._get_collection().update_many(
        pipe_match,
        pipe_set,
        upsert=True,
        array_filters=array_filters
    )
    print(f"bulk update using aggregate: {time.time() - t}")

    breakpoint()
