import os
import sys
import time

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import graphene
from graphene import Connection, ConnectionField, Node
from fastapi import FastAPI
from starlette.graphql import GraphQLApp

from models.base import User as UserModel


class UserNode(graphene.ObjectType):
    id = graphene.ID()
    first_name = graphene.String()
    last_name = graphene.String()

    class Meta:
        interface = (Node,)
    
    @classmethod
    def from_model(cls, model):
        return UserModel(id=model.id, first_name=model.first_name, last_name=model.last_name)


class UserConnection(Connection):
    class Meta:
        node = UserNode


class Query(graphene.ObjectType):
    users = ConnectionField(UserConnection)

    def resolve_users(self, info, **kwargs):
        return [UserNode.from_model(m) for m in UserModel.objects[1].histories]


schema = graphene.Schema(query=Query)


app = FastAPI(title="ContactQL", description="GraphQL Contact APIs", version="0.1")


@app.get("/")
async def root():
    return {"message": "Contact Applications!"}


app.add_route("/graphql", GraphQLApp(schema=graphene.Schema(query=Query)))


if __name__ == "__main__":
    """
    - uvicorn 4_1_cursor:app --host=0.0.0.0 --reload
    - python 4_1_cursor.py

    """
    t = time.time()
    UserModel.make_dateset()
    print(f"data setting time: {time.time() - t}")

    query = """
    query ($before:String, $after: String, $first: Int, $last: Int){
        users (before: $before, after: $after, first: $first, last: $last){
            pageInfo {
                hasNextPage
                hasPreviousPage
                startCursor
                hasNextPage
            }
            edges {
                cursor
                node {
                lastName
                id
                firstName
                }
            }
        }
    }
    """
    variables = {
        "first": 2
    }
    t = time.time()
    result = schema.execute(query, variables)
    print(f"data setting time: {time.time() - t}")

    # pp result.data

    breakpoint()
