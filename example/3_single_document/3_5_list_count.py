import os
import re
import sys
import time
import json
from collections import defaultdict

from mongoengine import Q

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from models.case_3 import BaseCase


if __name__ == '__main__':
    '''
    data setting time: 4.339810371398926
    bulk update at mongoengine: 3.357313632965088
    bulk update using aggregate: 0.036733388900756836
    약 90배 성능 향상
    Q(d__y__icontains="5-5-y").to_query(BaseCase)
    '''
    t = time.time()    
    BaseCase.make_dataset()
    print(f"data setting time: {time.time() - t}")

    #####################################################

    t = time.time()
    counts = defaultdict(lambda: 0)
    for idx, obj in enumerate(BaseCase.objects):
        for o in obj.d:
            if o.y == '5-5-y':
                counts[idx] += 1
    print(f"bulk update at mongoengine: {time.time() - t}")

    for i in range(0, 10):
        assert counts[5 + 10*i] == 100

    #######################################################

    _pipe = [
        {
            "$match": {}
        },
        {
            "$project": {
                "_id": 1,
                "arr": {
                    "$filter": {
                        "input": "$d",
                        "as": "item",
                        "cond": {
                            "$eq": ["$$item.y", '5-5-y']
                        }
                    }    
                }
            }
        },
        {
            "$addFields": {
                "count": {
                    "$size": "$arr"
                }
            }
        }
    ]

    t = time.time()
    results = list(
        BaseCase._get_collection().aggregate(
            _pipe
        )
    )
    print(f"bulk update using aggregate: {time.time() - t}")

    for i in range(0, 10):
        assert results[5 + 10*i]["count"] == 100

    breakpoint()
