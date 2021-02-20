from mongoengine import Document
from mongoengine.fields import StringField


class TestUser(Document):
    first_name = StringField()
    last_name = StringField()

    def __str__(self):
        return f"first name: {self.first_name}, last name: {self.last_name}"
