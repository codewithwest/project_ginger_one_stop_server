from ariadne import gql

from schemas.image_handler import image_handler_mutation, image_handler_query, image_handler_types
from schemas.youtube_downloader import youtube_downloader_types, youtube_downloader_queries, \
    youtube_downloader_mutations

type_definitions = gql(
    f"""
   {youtube_downloader_types}
   {image_handler_types}
    """
    +
   """type Query {"""+
    f"""
   {youtube_downloader_queries}
   {image_handler_query}
   """+
    """}"""+
    """type Mutation {""" +
    f"""
   {youtube_downloader_mutations}
   {image_handler_mutation}
    """+
    """}"""
)
