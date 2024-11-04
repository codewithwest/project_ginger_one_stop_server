from flask import jsonify
from yt_dlp import YoutubeDL
from graphql import  GraphQLError

class YouTubeDownloader:
    def __init__(self, download_link : str):
        self.formats_list = []
        self.download_link = download_link
        self.options = {}
        self.response_schema = {}

    def init_options(self):
        # Set options for the downloader
        self.options =  {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'outtmpl': '%(title)s.%(ext)s'  # Customize output filename
        }

    def get_all_available_formats(self, formats:list) -> list:

        for found_formats in formats:
            if found_formats['ext'] in ["webm", "mp4"]:
                self.formats_list.append(
                    {
                        "ext": found_formats.get('ext'),
                        "url": found_formats.get('url'),
                        "format": found_formats.get('format'),
                        "resolution": found_formats.get('resolution'),
                        "width": found_formats.get('width'),
                        "height": found_formats.get('height'),
                        "video_extension": found_formats.get('video_ext'),
                        "audio_extension": found_formats.get('audio_ext'),
                        "filesize_approx": found_formats.get('filesize_approx'),
                        "filesize": found_formats.get('filesize'),
                    }
                )

        return self.formats_list

    def generate_video_response_schema(self, video_info_dictionary: dict,found_video_formats:list) -> object:
        self.response_schema = {
            "title": video_info_dictionary.get('title'),
            "video_duration": video_info_dictionary.get('duration'),
            "ext": video_info_dictionary.get('ext'),
            "filesize_approx": video_info_dictionary.get('filesize_approx'),
            "highest_width": video_info_dictionary.get('width'),
            "highest_height": video_info_dictionary.get('height'),
            "highest_resolution": video_info_dictionary.get('resolution'),
            "webpage_url": video_info_dictionary.get('webpage_url'),
            "formats": found_video_formats,
        }


    def get_video_download_data(self):
        self.init_options()
        # # Create a YoutubeDL object and download the video
        with YoutubeDL(self.options) as youtube_downloader:
            try:
                video_info_dictionary = youtube_downloader.extract_info(self.download_link, download=False)
            except:
                raise GraphQLError('Sorry! Could not retrieve video info!')

        found_video_formats = self.get_all_available_formats(video_info_dictionary.get('formats'))
        self.generate_video_response_schema(video_info_dictionary, found_video_formats)


        print(self.response_schema)
        return  self.response_schema


