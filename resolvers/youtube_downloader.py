from flask import jsonify
from jinja2.lexer import Failure
from yt_dlp import YoutubeDL

class YouTubeDownloader:
    def __init__(self, request_link : str):
        self.options = None
        self.download_link = request_link

            # video_url = "https://www.youtube.com/watch?v=rY-DSC8U6sE"
    def init_options(self):

            # Set options for the downloader
            self.options  = {
                'format': 'best[ext=mp4]',
                'outtmpl': '%(title)s.%(ext)s'
            }
    def get_download_link(self):
        # # Create a YoutubeDL object and download the video
        print("The download link provided: ", self.download_link)
        with YoutubeDL(self.options) as you_tube_downloader:
            # try:
            print("Extracting media information... ")

            video_info = you_tube_downloader.extract_info(self.download_link, download=False)
            print("Media Title: ", video_info.get("title"))
            print("Media width: ", video_info.get("title"))
            print("Media Height: ", video_info.get("title"))

            # youtube_url = jsonify(video_info).get('url')
            print("The resolved url: ", video_info['formats'][-1]['url'])
            return video_info['formats'][-1]['url']
            # except:
            #     return  'An error has occured'


