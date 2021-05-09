from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import (
    StringField,
    EmbeddedDocumentListField,
    IntField,
)


class EmbeddedBaseCase(EmbeddedDocument):
    grouping_key = StringField()
    z = StringField()
    y = StringField()
    x = StringField()
    cnt = IntField()

    def __str__(self):
        return f"z: {self.z}, y: {self.y}, x: {self.x}, cnt: {self.cnt}"


class BaseCase(Document):
    a = StringField()
    b = StringField()
    c = StringField()
    d = EmbeddedDocumentListField(EmbeddedBaseCase)

    def __str__(self):
        return f"a: {self.a}, b: {self.b}, c: {self.c}, d: {self.d[:1]} * {len(self.d)}"

    @classmethod
    def make_dataset_mongoengine(cls):

        for i in range(5):
            for j in range(1000):
                try:
                    obj = cls.objects.get(a=f"a-{str(i).zfill(3)}", b=f"b-{str(i%10).zfill(3)}", c=f"c-{str(i%100).zfill(3)}")
                except:
                    obj = cls.objects.create(a=f"a-{str(i).zfill(3)}", b=f"b-{str(i%10).zfill(3)}", c=f"c-{str(i%100).zfill(3)}", d=[])

                embd_obj = obj.d.filter(grouping_key=f"y-{j%10}%x-{j%7}")

                if not embd_obj:
                    obj.d.append(EmbeddedBaseCase(grouping_key=f"y-{j%10}%x-{j%7}", z=f"z-{j}", y=f"y-{j%10}", x=f"x-{j%10}", cnt=1))
                else:
                    embd_obj[0].cnt += 1
                obj.save()
