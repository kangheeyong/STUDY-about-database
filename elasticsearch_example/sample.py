import time

import pymongo


__conn = pymongo.MongoClient("mongodb://mongodb1:27017,mongodb2:27017,mongodb3:27017")

__db = __conn.get_database("test")
test_collection = __db.get_collection("test_collection")

maxCnt = 10

for idx in range(0, maxCnt):
    test_collection.insert_one(
        {
            "number": 123,
            "hash": "0x1234567",
            "array": [1, 2, 3, 4],
            "timestamp": time.time(),
        }
    )
    print(f"======= {idx}/{maxCnt} success")
    time.sleep(0.5)
