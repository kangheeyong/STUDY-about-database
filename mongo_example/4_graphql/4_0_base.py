import os
import sys
import time

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import graphene
from fastapi import FastAPI
from starlette.graphql import GraphQLApp
from graphene_mongo import MongoengineObjectType

from models.base import User as UserModel


class User(MongoengineObjectType):
    class Meta:
        model = UserModel


class Query(graphene.ObjectType):
    users = graphene.List(User)

    def resolve_users(self, info):
        return list(UserModel.objects.all())


schema = graphene.Schema(query=Query)


app = FastAPI(title="ContactQL", description="GraphQL Contact APIs", version="0.1")


@app.get("/")
async def root():
    return {"message": "Contact Applications!"}


app.add_route("/graphql", GraphQLApp(schema=graphene.Schema(query=Query)))


if __name__ == "__main__":
    """
    - uvicorn 4_0_base:app --host=0.0.0.0 --reload
    - python 4_0_base.py

    """
    t = time.time()
    UserModel.make_dateset()
    print(f"data setting time: {time.time() - t}")

    query = """
        query {
            users {
                firstName,
                lastName
            }
        }
    """

    t = time.time()
    result = schema.execute(query)
    print(f"data setting time: {time.time() - t}")

    # pp result.data

    breakpoint()
