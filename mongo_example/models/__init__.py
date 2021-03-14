import os
from mongoengine import connect
from pymongo.read_preferences import ReadPreference


connect(
    os.environ.get("MONGO_DB_NAME"),
    host=os.environ.get("MONGO_HOST"),
    replicaset="rp0",
    read_preference=ReadPreference.SECONDARY_PREFERRED,
)
