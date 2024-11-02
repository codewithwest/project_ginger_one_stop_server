from yt_dlp import YoutubeDL

from resolvers.main_resolver import query
from schemas.type_definitions import type_definitions
from ariadne import make_executable_schema, graphql_sync
from flask import Flask, jsonify,  request, render_template


app = Flask(__name__)

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



app = Flask(__name__, template_folder="pages/templates")


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def index_post():
    options = {
        'format': 'best[ext=mp4]',
        'outtmpl': '%(title)s.%(ext)s'
    }
    yt = request.form['text']
    YoutubeDL(options).download(yt)
    # base, ext = os.path.splitext(out_file)
    # new_file = base + '.mp3'
    # os.rename(out_file, new_file)
    return render_template('results.html')

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
