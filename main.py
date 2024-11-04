from io import BytesIO

import flask
from Cryptodome.Util.RFC1751 import binary
from yt_dlp import YoutubeDL
import requests
from resolvers.main_resolver import query
from schemas.type_definitions import type_definitions
from ariadne import make_executable_schema, graphql_sync
from flask import Flask, jsonify, request, render_template, send_file, make_response, Response

app = Flask(__name__, template_folder="pages/templates")

ALLOWED_ORIGINS = ['*']
# from ariadne.constants import PLAYGROUND_HTML

# Create executable schema
schema = make_executable_schema(type_definitions, query)


# Create a GraphQL Playground UI for the GraphQL schema

# @app.route("/graphql", methods=["GET"])
# def graphql_playground():
# Playground accepts GET requests only.
# If you wanted to support POST you'd have to
# change the method to POST and set the content
# type header to application/graphql
# return PLAYGROUND_HTML

# Create a GraphQL endpoint for executing GraphQL queries

@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()

    success, result = graphql_sync(
        schema, data, context_value={"request": request})
    status_code = 200 if success else 400
    return jsonify(result), status_code


# app = Flask(__name__)
#
# app.config["IMAGE_UPLOADS"] = "/home/west/Documents/west/youtube-scraper/static/images"
#
# # Route to upload image
# @app.route('/upload-image', methods=['GET', 'POST'])
# def upload_image():
#     if request.method == "POST":
#         if request.files:
#             image = request.files["image"]
#             print(image)
#             image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
#             return redirect(request.url)
#     return render_template("upload_image.html")
#
#

# app = Flask(__name__)





@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")


# def index():
#     # video_url = request.args.get('url')
#     video_url = "https://www.youtube.com/watch?v=KEUUKA3fuaQ"
#     # if not video_url:
#     #     return jsonify({'error': 'Missing video URL'}), 400

#     # Check for allowed origin (if applicable)
#     origin = request.headers.get('Origin')
#     if origin and origin not in ALLOWED_ORIGINS:
#         return make_response(jsonify({'error': 'CORS not allowed'}), 403)

#     options = {
#         'format': 'best[ext=mp4]',
#         'outtmpl': '%(title)s.%(ext)s'
#     }
#     with YoutubeDL(options) as ydl:

#         info_dict = ydl.extract_info(video_url, download=False)
#         video_url = info_dict['url']

#         response = requests.get("https://manifest.googlevideo.com/api/manifest/hls_variant/expire/1730605908/ei/9J4mZ7HsGKDQp-oPiqDuqQg/ip/105.245.116.122/id/2e36717929deebb1/source/youtube/requiressl/yes/xpc/EgVo2aDSNQ%3D%3D/playback_host/rr2---sn-8vq5jvh15-2gts.googlevideo.com/met/1730584308%2C/mh/1M/mm/31%2C29/mn/sn-8vq5jvh15-2gts%2Csn-8vq5jvh15-wocl/ms/au%2Crdu/mv/m/mvi/2/pl/22/rms/au%2Cau/tx/51241482/txs/51241481%2C51241482%2C51241483%2C51241484%2C51241485%2C51241486/hfr/1/demuxed/1/tts_caps/1/maudio/1/pcm2/no/initcwndbps/516250/vprv/1/go/1/rqh/5/mt/1730583896/fvip/3/nvgoi/1/short_key/1/ncsapi/1/keepalive/yes/fexp/51312688%2C51326932/dover/13/itag/0/playlist_type/DVR/sparams/expire%2Cei%2Cip%2Cid%2Csource%2Crequiressl%2Cxpc%2Ctx%2Ctxs%2Chfr%2Cdemuxed%2Ctts_caps%2Cmaudio%2Cpcm2%2Cvprv%2Cgo%2Crqh%2Citag%2Cplaylist_type/sig/AJfQdSswRQIgRpUOvwLFNXCe5TWzDe2K17vfaXN3zLvkJL0fdl_decACIQDyVDIPVKty8bP6I0VY87eyxPfbZAWEik8N62vuRAR-zg%3D%3D/lsparams/playback_host%2Cmet%2Cmh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Crms%2Cinitcwndbps/lsig/ACJ0pHgwRgIhAJyFIlNvmq993P1bGpwUd3ZNrMZ31PxHJhksk-5YpuimAiEAjePr_jso7nbV1edawT6SC1t_TVex2PYdu1J6EQDGXQs%3D/file/index.m3u8", stream=True)
#         response.raise_for_status()

#         content_type = response.headers.get('Content-Type')

#         # Create a response object
#         response_obj = make_response(response.content, 200)

#         # Set Content-Disposition and Content-Type headers
#         response_obj.headers.set('Content-Disposition', f'attachment; filename="{"filename"}"')
#         response_obj.headers.set('Content-Type', content_type)

#         # Add CORS headers (if necessary)
#         if origin:
#             response_obj.headers.set('Access-Control-Allow-Origin', origin)
#             response_obj.headers.set('Access-Control-Allow-Methods', 'GET')
#             response_obj.headers.set('Access-Control-Allow-Headers', 'Content-Type')

#         return response_obj
#     # except requests.exceptions.RequestException as e:
#     #     print(f"Error fetching video: {e}")
#     #     return jsonify({'error': 'Error fetching video'}), 500


@app.route('/', methods=['POST'])
def index_post():
    options = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': '%(title)s.%(ext)s'  # Customize output filename
    }
    yt = request.form['text']

    ydl_opts = {'format': 'best',
                'download_sections': "*00:00:00-00:00:10",
                'force_keyframes_at_cuts': True,
                }

    with  YoutubeDL(options) as ydl:
        video_info_dictionary = ydl.extract_info(yt, download=False)

    # if video_info_dictionary["formats"]:
    #     video_info_dictionary = video_info_dictionary['formats']
        # return info_dict['formats'][-1]['url']
    # return render_template('results.html')
    # return (video_info_dictionary)
        formats_list = []
        for found_formats in video_info_dictionary.get('formats'):
            if found_formats['ext'] in ["webm", "mp4"]:
                formats_list.append(
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
        response_schema = {
            "title": video_info_dictionary.get('title'),
            "video_duration": video_info_dictionary.get('duration'),
            "ext": video_info_dictionary.get('ext'),
            "filesize_approx": video_info_dictionary.get('filesize_approx'),
            "highest_width": video_info_dictionary.get('width'),
            "highest_height": video_info_dictionary.get('height'),
            "highest_resolution": video_info_dictionary.get('resolution'),
            "webpage_url": video_info_dictionary.get('webpage_url'),
            "formats":formats_list,
        }






        return jsonify({"data": response_schema})

# def get_download_link(self):
# # Create a YoutubeDL object and download the video
# with YoutubeDL(options) as you_tube_downloader:
#     # try:
#     # video_info = you_tube_downloader.extract_info("https://www.youtube.com/watch?v=qvS8jM6nxz8&list=RDqvS8jM6nxz8&start_radio=1", download=False)
#     # video_title = video_info.get("title")
#     try:
#         you_tube_downloader.download("https://www.youtube.com/watch?v=qvS8jM6nxz8&list=RDqvS8jM6nxz8&start_radio=1")
#     except:
#         print("Something went wrong")

# width = video_info.get("width")
# height = video_info.get("height")
# language = video_info.get("language")
# channel = video_info.get("channel")
# likes = video_info.get("like_count")
# print(video_info.keys())
# print)
# youtube_url = jsonify(video_info).get('url')
# print("The resolved url: ",video_title)
# return video_info['formats'][-1]['url']
# except:
#     return  'An error has occured'
# return render_template("index.html")


# @app.route('/success', methods=['POST'])
# def success():
#     if request.method == 'POST':
#         f = request.files['file']
#         f.save(f.filename)
#         return render_template("Acknowledgement.html", name=f.filename)


if __name__ == '__main__':
    app.run(debug=True)
