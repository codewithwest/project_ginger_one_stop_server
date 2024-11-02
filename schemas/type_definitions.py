from ariadne import gql
from schemas.youtube_downloader import youtube_downloader_types, youtube_downloader_queries, \
    youtube_downloader_mutations

type_definitions = gql(
    f"""
    {youtube_downloader_types}

    {youtube_downloader_queries}

    {youtube_downloader_mutations}
    """
)
