from resolvers.main_resolver import query
from resolvers.youtube_downloader import YouTubeDownloader
from schemas.type_definitions import type_definitions
from ariadne import make_executable_schema, graphql_sync
from flask import Flask, jsonify, request, render_template

app = Flask(__name__, template_folder="pages/templates")

ALLOWED_ORIGINS = ['*']
# from ariadne.constants import PLAYGROUND_HTML

# Create executable schema
schema = make_executable_schema(type_definitions, query)

@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()

    success, result = graphql_sync(
        schema, data, context_value={"request": request})
    status_code = 200 if success else 400
    return jsonify(result), status_code

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")
@app.route('/', methods=['POST'])
def index_post():
    link = request.form['text']

    return jsonify({"data": YouTubeDownloader(link).get_video_download_data()})

if __name__ == '__main__':
    app.run(debug=True)
