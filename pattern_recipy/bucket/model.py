from __future__ import annotations # mongoengine Document를 typing으로 하기 휘새 필요하다

import os
import random
from typing import Optional, Type, TypeVar, Generic, Union
from datetime import datetime, timedelta

from mongoengine import connect, QuerySet, Document, EmbeddedDocument, DoesNotExist
from mongoengine.fields import *


connect(os.environ.get('MONGO_DB_NAME', "test"), host=os.environ.get('MONGO_HOST' ""))


NOW = datetime(2021, 3, 7, 0, 0, 0)
SECOND = 0
DELETE_COUNT = 200


U = TypeVar("U", bound=Document)


class QuerySetManager(Generic[U]):
    def __get__(self, instance: object, cls: Type[U]) -> QuerySet[U]:
        return QuerySet(cls, cls._get_collection())


class Measurement(EmbeddedDocument):
    time_stamp = DateTimeField()
    temperature = FloatField()

    def __str__(self):
        return f"time_stamp: {self.time_stamp}, temperature: {self.temperature}"


class BucketPattern(Document):
    date_time = DateTimeField(default=datetime.utcnow)
    measurements = EmbeddedDocumentListField(Measurement)
    count = IntField(default=0)

    objects = QuerySetManager["BucketPattern"]()

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
            for j in range(0, random.randint(600, 3599)):
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
    def get_obj(cls, date_time: datetime=NOW - timedelta(days=1)) -> Optional[BucketPattern]:
        try:
            return cls.objects.get(date_time=date_time)
        except DoesNotExist:
            return None

    @classmethod
    def update_using_mongoengine_v1(cls, temperature: int, date_time: datetime=NOW):
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
    def update_using_mongoengine_v2(cls, temperature: int, date_time: datetime=NOW):
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
    def update_using_pymongo(cls, temperature: int, date_time: datetime=NOW):
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

    @classmethod
    def delete_using_mongoengine_v1(cls, date_time: datetime=NOW - timedelta(days=1)):
        try:
            obj = cls.objects.get(date_time=date_time)
        except DoesNotExist:
            obj = cls.objects.create(date_time=date_time)

        for idx in range(len(obj.measurements)-1, -1, -1):
            if obj.measurements[idx].time_stamp < NOW - timedelta(days=1) + timedelta(seconds=DELETE_COUNT):
                del obj.measurements[idx]
                obj.count -= 1
        obj.save()

    @classmethod
    def delete_using_pymongo(cls, date_time: datetime=NOW - timedelta(days=1)):
        global SECOND

        _filter = {'date_time': date_time}
        _update = {
            "$pull": {
                "measurements": {
                    "time_stamp": {
                        "$lt": NOW - timedelta(days=1) + timedelta(seconds=DELETE_COUNT)
                    }
                }
            }
        }
        cls._get_collection().update_one(
            _filter,
            _update,
        )

        # cls._get_collection().update_one(
        #     _filter,
        #     {
        #         "$addFields": {
        #             "count": {
        #                 "$size": "$measurements"
        #             }
        #         }
        #     },
        #     upsert=True
        # )

        SECOND += 1
