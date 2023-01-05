import graphene

import app_demo_grapql.schema


class Query(app_demo_grapql.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

schema = graphene.Schema(query=Query)