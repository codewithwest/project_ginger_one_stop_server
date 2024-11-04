
from ariadne import QueryType

from resolvers.youtube_downloader import YouTubeDownloader

query = QueryType()

# Define resolvers

@query.field("getYouTubeVideoDownloadData")
def download_link(_root, info, link):

    return [YouTubeDownloader(link).get_video_download_data()]
