import time

from model import BucketPattern, DELETE_COUNT


if __name__ == "__main__":
    """
    bucket parrtern example
    1.
        data setting time: 8.04081416130066
        update at mongoengine_v1: 0.15709495544433594

    2.
        data setting time: 7.521857976913452
        delete at pymongo: 0.002148866653442383

    약 75배 속도향상

    # TODO: delete_using_pymongo에서 list size를 동시에 업데이트하는 방법을 찾아보자

    - mongoshell
        `db.bucket_pattern.find({}).sort({date_time: -1}).limit(1).pretty()`

    """
    t = time.time()
    BucketPattern.make_dataset()
    print(f"data setting time: {time.time() - t}")

    ################################################

    count = BucketPattern.get_obj().count

    t = time.time()
    BucketPattern.delete_using_mongoengine_v1()
    print(f"update at mongoengine_v1: {time.time() - t}")

    assert count == BucketPattern.get_obj().count + DELETE_COUNT

    ##################################################

    # count = BucketPattern.get_obj().count

    # t = time.time()
    # BucketPattern.delete_using_pymongo()
    # print(f"delete at pymongo: {time.time() - t}")

    # assert count == BucketPattern.get_obj().count + DELETE_COUNT

    breakpoint()