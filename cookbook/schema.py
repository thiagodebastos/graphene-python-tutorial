from graphene import Schema, ObjectType
from cookbook.ingredients.schema import Query

class Query(Query, ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

schema = Schema(query=Query)
