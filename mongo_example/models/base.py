from bson import ObjectId

from mongoengine import Document, EmbeddedDocument
from mongoengine.fields import StringField, EmbeddedDocumentListField, ObjectIdField


class History(EmbeddedDocument):
    id = ObjectIdField(required=True)
    first_name = StringField(required=True)
    last_name = StringField(required=True)

    def __str__(self):
        return f"_id: {self._id}, a: {self.a}, b: {self.b}"


class User(Document):
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    histories = EmbeddedDocumentListField(History)

    def __str__(self):
        return f"id: {self.id}, first name: {self.first_name}, last name: {self.last_name}, histories: {self.histories[:1]} * {len(self.histories)}"

    @classmethod
    def make_dateset(cls):
        cls.objects.delete()
        for i in range(5):
            cls.objects.create(
                first_name=f"first-{i}",
                last_name=f"last-{i}",
                histories=[
                    History(
                        id=ObjectId(), first_name=f"a-{j}-{i}", last_name=f"b-{j}-{i}"
                    )
                    for j in range(10)
                ],
            )
