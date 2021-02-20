import os
from mongoengine import connect


connect(os.environ.get('MONGO_DB_NAME'), host=os.environ.get('MONGO_HOST'))
