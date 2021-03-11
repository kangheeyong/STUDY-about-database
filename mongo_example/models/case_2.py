from typing import Type

from mongoengine import Document
from mongoengine.fields import StringField, LazyReferenceField


class BaseCase1:
    a = StringField()
    b = StringField()
    c = StringField()

    def __str__(self):
        return f"a: {self.a}, b: {self.b}, c: {self.c}"


class BaseCase2:
    a = StringField()
    b = StringField()
    c = StringField()

    def __str__(self):
        return f"a: {self.a}, b: {self.b}, c: {self.c}"


class Case1_1(Document, BaseCase1):
    pass


class Case1_2(Document, BaseCase2):
    d = LazyReferenceField(Case1_1)

    def __str__(self):
        return f"a: {self.a}, b: {self.b}, c: {self.c}, d: {self.d}"


def make_dateset(model_1: Type[Case1_1], model_2: Type[Case1_2]):
    model_1.objects.delete()
    model_2.objects.delete()
    for i in range(10000):
        obj = model_1.objects.create(a=f"1-a-{i}", b=f"1-b-{i%10}", c=f"1-c-{i%100}")
        model_2.objects.create(a=f"2-a-{i}", b=f"2-b-{i%10}", c=f"2-c-{i%100}", d=obj)
