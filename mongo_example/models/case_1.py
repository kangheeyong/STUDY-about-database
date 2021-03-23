from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import StringField, EmbeddedDocumentListField


class EmbeddedBaseCase(EmbeddedDocument):
    z = StringField()

    def __str__(self):
        return f"z: {self.z}"


class BaseCase(object):
    a = StringField()
    b = StringField()
    c = StringField()
    d = EmbeddedDocumentListField(EmbeddedBaseCase)

    def __str__(self):
        return f"a: {self.a}, b: {self.b}, c: {self.c}"

    @classmethod
    def make_dateset(cls):
        cls.objects.delete()
        for i in range(10000):
            cls.objects.create(a=f"a-{i}", b=f"b-{i%10}", c=f"c-{i%100}")

    @classmethod
    def make_dateset_v6(cls):
        cls.objects.delete()
        for i in range(10000):
            cls.objects.create(
                a=f"a-{i}",
                b=f"b-{i%10}",
                c=f"c-{i%100}",
                d=[EmbeddedBaseCase(z=str(i))] + [EmbeddedBaseCase(z=f"e-{j}") for j in range(100)],
            )


class Case1(Document, BaseCase):
    pass


class Case2(Document, BaseCase):
    meta = {"indexes": ["c"]}


class Case3(Document, BaseCase):
    meta = {"indexes": [("c", "a")]}


class Case4(Document, BaseCase):
    meta = {"indexes": [("a", "c")]}


class Case5(Document, BaseCase):
    meta = {"indexes": [("_id", "a")]}


class Case6(Document, BaseCase):
    meta = {"indexes": [("d.z")]}
