import os
import re
import sys
import time
import json

from mongoengine import Q

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from models.case_3 import BaseCase1


if __name__ == "__main__":
    """
    1.
        data setting time: 14.760640859603882
        bulk update at mongoengine: 0.008388519287109375
    2.
        data setting time: 14.341774463653564
        bulk update using pymongo: 0.03893399238586426
    """
    t = time.time()
    BaseCase1.make_dataset()
    print(f"data setting time: {time.time() - t}")

    query = 'b-50'

    #######################################################
    t = time.time()
    for obj in BaseCase1.objects(b__in=query):
        del obj.b[query]
        obj.save()
    print(f"bulk update at mongoengine: {time.time() - t}")

    #######################################################
    #   cls.objects(
    #       **{"project": project, f"search_sdk_faq_feedback_history__{faq_id}__exists": 1}
    #   ).update(**{f"unset__search_sdk_faq_feedback_history__{faq_id}": 1})
    #
    #######################################################
    # _filter = {f"b.{query}": {"$exists": True}}
    # _unset = {"$unset": f"b.{query}"}

    # t = time.time()
    # obj = BaseCase1._get_collection().update_many(_filter, [_unset])
    # print(f"bulk update using pymongo: {time.time() - t}")

    breakpoint()
