from mongoengine import Document
from mongoengine.fields import StringField


class BaseCase(object):
    a = StringField()
    b = StringField()
    c = StringField()

    def __str__(self):
        return f"a: {self.a}, b: {self.b}, c: {self.c}"

    @classmethod
    def make_dateset(cls):
        cls.objects.delete()
        for i in range(10000):
            cls.objects.create(a=f"a-{i}", b=f"b-{i%10}", c=f"c-{i%100}")


class Case1(Document, BaseCase):
    pass


class Case2(Document, BaseCase):
    meta = {
        'indexes': [
           'c' 
        ]
    }


class Case3(Document, BaseCase):
    meta = {
        'indexes': [
           ('c', 'a') 
        ]
    }


class Case4(Document, BaseCase):
    meta = {
        'indexes': [
           ('a', 'c') 
        ]
    }
