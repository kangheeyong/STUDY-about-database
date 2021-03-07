import time

from model import BucketPattern, DELETE_COUNT


if __name__ == '__main__':
    '''
    bucket parrtern example

    # TODO: delete_using_pymongo에서 list size를 동시에 업데이트하는 방법을 찾아보자

    - mongoshell
        `db.bucket_pattern.find({}).sort({date_time: -1}).limit(1).pretty()`

    '''
    t = time.time()    
    BucketPattern.make_dataset()
    print(f"data setting time: {time.time() - t}")

################################################

    # count = BucketPattern.get_obj().count
    
    # t = time.time()
    # BucketPattern.delete_using_mongoengine_v1()
    # print(f"update at mongoengine_v1: {time.time() - t}")
    
    # assert count == BucketPattern.get_obj().count + DELETE_COUNT

##################################################

    count = BucketPattern.get_obj().count
    
    t = time.time()
    BucketPattern.delete_using_pymongo()
    print(f"delete at pymongo: {time.time() - t}")
    
    # assert count == BucketPattern.get_obj().count + DELETE_COUNT
    # len(BucketPattern.get_obj().measurements)

    breakpoint()