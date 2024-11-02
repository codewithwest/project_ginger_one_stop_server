
from ariadne import QueryType

from resolvers.youtube_downloader import YouTubeDownloader

query = QueryType()

# Define resolvers

@query.field("getDownloadLink")
def download_link(_root, info, link):

    print("Info: ", info)

    resolved_download_link = YouTubeDownloader(link).get_download_link()
    return [
        {
            "download_link": resolved_download_link,
        }
    ]