from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import (
    StringField,
    EmbeddedDocumentListField,
    DictField,
    ListField,
)


class EmbeddedBaseCase(EmbeddedDocument):
    z = StringField()
    y = StringField()
    x = StringField()

    def __str__(self):
        return f"z: {self.z}, y: {self.y}, x: {self.x}"


class BaseCase(Document):
    a = StringField()
    b = StringField()
    c = StringField()
    d = EmbeddedDocumentListField(EmbeddedBaseCase)
    e = DictField()
    f = ListField()
    g = ListField(StringField())

    def __str__(self):
        return f"a: {self.a}, b: {self.b}, c: {self.c}, d: {self.d[:1]} * {len(self.d)}, e: {self.e[:1]}, g: {self.g[:1]}"

    @classmethod
    def make_dataset(cls):
        cls.objects.delete()

        for i in range(100):
            embd = []
            for j in range(1000):
                embd.append(
                    EmbeddedBaseCase(
                        z=f"{i}-{j}-z",
                        y=f"{i%10}-{j%10}-y",
                        x=f"{i%100}-{j%100}-x",
                    )
                )

            cls.objects.create(
                a=f"a-{i}",
                b=f"b-{i%10}",
                c=f"c-{i%100}",
                d=embd,
                e={"e_1": f"a-{i}", "e_2": f"a-{i%10}", "e_3": f"a-{i%100}"},
                f=[i for i in range(5)],
                g=[str(i) for i in range(1000)],
            )
