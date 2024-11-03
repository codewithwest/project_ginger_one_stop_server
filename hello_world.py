from ariadne.asgi import GraphQL
from ariadne import gql, QueryType, make_executable_schema, MutationType

from schemas import type_definitions

# Define type definitions (schema) using SDL
# type_defs = gql(
#     """
#    type Query {
#        places: [Place]
#    }


#    type Place {
#        name: String!
#        description: String!
#        country: String!
#        }
#    """
# )

# Initialize query

query = QueryType()

# Define resolvers
mutation = MutationType()

@query.field("get_download_link")
def get_download_link(*_):
    return [
        {"name": "Paris", "description": "The city of lights", "country": "France"},
        {"name": "Rome", "description": "The city of pizza", "country": "Italy"},
        {
            "name": "London",
            "description": "The city of big buildings",
            "country": "United Kingdom",
        },
    ]


# Create executable schema
schema = make_executable_schema(type_definitions, [query, mutation])

# Create ASGI application
app = GraphQL(schema)
