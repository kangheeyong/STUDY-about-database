from mongoengine import Document
from mongoengine.fields import StringField

class User(Document):
    first_name = StringField(required=True)
    last_name = StringField(required=True)

    meta = {'collection': 'user'}

    @classmethod
    def make_dateset(cls):
        cls.objects.delete()
        for i in range(100):
            cls.objects.create(first_name=f"first-{i}", last_name=f"last-{i}")
