from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import StringField, EmbeddedDocumentListField


class EmbeddedBaseCase(EmbeddedDocument):
    z = StringField()
    y = StringField()
    x = StringField()

    def __str__(self):
        return f"z: {self.z}, x: {self.x}"


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
                d=[EmbeddedBaseCase(z=str(i))]
                + [EmbeddedBaseCase(z=f"e-{j}") for j in range(100)],
            )

    @classmethod
    def make_dateset_v7(cls):
        cls.objects.delete()
        for i in range(100):
            obj = cls(
                a=f"a-{i}",
                b=f"b-{i%10}",
                c=f"c-{i%100}",
                d=[
                    EmbeddedBaseCase(z=f"e-{j%100}", y=f"e-{(j+1)%100}", x="1")
                    for j in range(100)
                ],
            )
            if i == 50:
                obj.d.append(EmbeddedBaseCase(z="e-50", y="e-50", x="1"))
            obj.save()

    @classmethod
    def make_dateset_v8(cls):
        cls.objects.delete()
        for i in range(100):
            obj = cls(
                a=f"a-{i}",
                b=f"b-{i%10}",
                c=f"c-{i%100}",
                d=[
                    EmbeddedBaseCase(z=f"f-{i}-{j}", y=f"f-{i}-{j}", x="1")
                    for j in range(100)
                ],
            )
            if i == 50:
                obj.d.append(EmbeddedBaseCase(z="e-50", y="e-50", x="1"))
            obj.save()


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


class Case7(Document, BaseCase):
    meta = {
        "indexes": [
            {
                "fields": ("d.y", "d.z"),
                "partialFilterExpression": {
                    "d.y": {"$type": "string"},
                    "x.z": {"$type": "string"},
                },
            }
        ]
    }


class Case7_1(Document, BaseCase):
    meta = {"indexes": [{"fields": ("d.y", "d.z")}]}


class Case8(Document, BaseCase):
    meta = {
        "indexes": [
            {
                "fields": ("d.y", "d.z"),
                "partialFilterExpression": {
                    "d.y": {"$type": "string"},
                    "x.z": {"$type": "string"},
                },
                "unique": True,
            }
        ]
    }


class Case8_1(Document, BaseCase):
    meta = {"indexes": [{"fields": ("d.y", "d.z"), "unique": True}]}
