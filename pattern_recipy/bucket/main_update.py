import time

from model import BucketPattern, NOW


if __name__ == "__main__":
    """
    bucket parrtern example
    1.
        data setting time: 7.646545886993408
        bulk update at mongoengine_v1 first: 0.009556770324707031
        bulk update at mongoengine_v1 * 1000: 30.201674461364746
        bulk update at mongoengine_v1 after 1001: 0.058678388595581055
    2.
        data setting time: 7.5592076778411865
        bulk update at mongoengine_v2 first: 0.006579160690307617
        bulk update at mongoengine_v2 * 1000: 14.078705549240112
        bulk update at mongoengine_v2 after 1001: 0.03003716468811035
    3.
        data setting time: 7.1907525062561035
        bulk update at pymongo first: 0.0014126300811767578
        bulk update using pymongo: 0.9429209232330322
        bulk update at pymongo after 1001: 0.0013148784637451172

    mongoengine으로 업데이트를 하는 경우 속도 저하의 문제가 있었다.
    하지만 pymongo로 직접 업데이트 할 경우 속도 저하의 문제가 발생하지 않았다.

    - mongoshell
        `db.bucket_pattern.find({}).sort({date_time: -1}).limit(1).pretty()`

    """
    t = time.time()
    BucketPattern.make_dataset()
    print(f"data setting time: {time.time() - t}")

    ################################################

    # t = time.time()
    # BucketPattern.update_using_mongoengine_v1(temperature=23)
    # print(f"bulk update at mongoengine_v1 first: {time.time() - t}")

    # t = time.time()
    # for _ in range(1000):
    #     BucketPattern.update_using_mongoengine_v1(temperature=23)
    # print(f"bulk update at mongoengine_v1 * 1000: {time.time() - t}")

    # t = time.time()
    # BucketPattern.update_using_mongoengine_v1(temperature=23)
    # print(f"bulk update at mongoengine_v1 after 1001: {time.time() - t}")

    # assert 1002 == BucketPattern.objects.get(date_time=NOW).count

    ################################################

    # t = time.time()
    # BucketPattern.update_using_mongoengine_v2(temperature=23)
    # print(f"bulk update at mongoengine_v2 first: {time.time() - t}")

    # t = time.time()
    # for _ in range(1000):
    #     BucketPattern.update_using_mongoengine_v2(temperature=23)
    # print(f"bulk update at mongoengine_v2 * 1000: {time.time() - t}")

    # t = time.time()
    # BucketPattern.update_using_mongoengine_v2(temperature=23)
    # print(f"bulk update at mongoengine_v2 after 1001: {time.time() - t}")

    # assert 1002 == BucketPattern.objects.get(date_time=NOW).count

    ##################################################

    t = time.time()
    BucketPattern.update_using_pymongo(temperature=23)
    print(f"bulk update at pymongo first: {time.time() - t}")

    t = time.time()
    for _ in range(1000):
        BucketPattern.update_using_pymongo(temperature=23)
    print(f"bulk update using pymongo: {time.time() - t}")

    t = time.time()
    BucketPattern.update_using_pymongo(temperature=23)
    print(f"bulk update at pymongo after 1001: {time.time() - t}")

    assert 1002 == BucketPattern.objects.get(date_time=NOW).count

    breakpoint()