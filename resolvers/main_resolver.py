
from ariadne import QueryType, MutationType


from resolvers.youtube_downloader import YouTubeDownloader

query = QueryType()
mutation = MutationType()
# Define resolvers

@query.field("getYouTubeVideoDownloadData")
def download_link(_root, info, link):
    data = YouTubeDownloader(link).get_video_download_data()
    return [data]
