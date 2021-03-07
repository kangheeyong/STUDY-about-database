import os
import random
from datetime import datetime, timedelta

from mongoengine import connect, Document, EmbeddedDocument, DoesNotExist
from mongoengine.fields import *


connect(os.environ.get('MONGO_DB_NAME'), host=os.environ.get('MONGO_HOST'))


NOW = datetime(2021, 3, 7, 0, 0, 0)
SECOND = 0

class Measurement(EmbeddedDocument):
    time_stamp = DateTimeField()
    temperature = FloatField()

    def __str__(self):
        return f"time_stamp: {self.time_stamp}, temperature: {self.temperature}"


class BucketPattern(Document):
    date_time = DateTimeField(default=datetime.utcnow)
    measurements = EmbeddedDocumentListField(Measurement)
    count = IntField(default=0)

    meta = {
        'indexes': [
           '-date_time'
        ]
    }

    def __str__(self):
        return f"date_time: {self.date_time}, measurements: {self.measurements[:1]}, count: {self.count}"
    
    @classmethod
    def make_dataset(cls):
        cls.objects.delete()
        
        for i in range(100, 0, -1):
            days = NOW - timedelta(days=i)
            embd = []
            for j in range(0, random.randint(0, 3599)):
                embd.append(
                    Measurement(
                        time_stamp = days + timedelta(seconds=j),
                        temperature = random.randint(30, 40)
                    )
                )
                
            cls.objects.create(
                date_time=days,
                measurements=embd,
                count=len(embd)
            )

    @classmethod
    def update_using_mongoengine_v1(cls, temperature, date_time=NOW):
        global SECOND

        try:
            obj = cls.objects.get(date_time=date_time)
        except DoesNotExist:
            obj = cls.objects.create(date_time=date_time)

        obj.measurements.append(
            Measurement(
                time_stamp = date_time + timedelta(seconds=SECOND),
                temperature = random.randint(30, 40)
            )
        )
        obj.count += 1
        obj.save()

        SECOND += 1

    @classmethod
    def update_using_mongoengine_v2(cls, temperature, date_time=NOW):
        global SECOND

        try:
            obj = cls.objects.get(date_time=date_time)
        except DoesNotExist:
            obj = cls.objects.create(date_time=date_time)

        obj.update(
            push__measurements=Measurement(
                time_stamp = date_time + timedelta(seconds=SECOND),
                temperature = random.randint(30, 40)
            ),
            inc__count=1
        )

        SECOND += 1

    @classmethod
    def update_using_pymongo(cls, temperature, date_time=NOW):
        global SECOND
        
        _filter = {'date_time': date_time}
        _update = {
            "$push": {
                "measurements": Measurement(
                    time_stamp = date_time + timedelta(seconds=SECOND),
                    temperature = random.randint(30, 40)
                ).to_mongo()
            },
            "$inc": {
                "count": 1
            }
        }
        cls._get_collection().update_one(
            _filter,
            _update,
            upsert=True
        )

        SECOND += 1

