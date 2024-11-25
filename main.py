from flask_cors import CORS, cross_origin
from resolvers.image_handler import ImageConverter
from resolvers.main_resolver import query
from resolvers.youtube_downloader import YouTubeDownloader
from schemas.type_definitions import type_definitions
from flask import Flask, jsonify, request, render_template
from ariadne import make_executable_schema, graphql_sync, upload_scalar
import base64

app = Flask(__name__, template_folder="pages/templates")
CORS(
    app,
    supports_credentials=True,
    allow_headers=[
        'Content-Type',
        'Authorization'
    ],
)

ALLOWED_ORIGINS = ['*']
# Create executable schema
schema = make_executable_schema(type_definitions, [query, upload_scalar])

@app.route("/graphql", methods=["POST"])
@cross_origin(origins='*')
def graphql_server():
    if request.is_json:
        data = request.get_json()
    else:
        data = request.values

    success, result = graphql_sync(
        schema, data, context_value={"request": request})
    status_code = 200 if success else 400

    return jsonify(result), status_code

@app.route('/uploadImage', methods=['POST'])
@cross_origin(origins='*')
def upload_image():
    if  len(request.files) == 0 and not request.form.get('file'):
        return jsonify({'error': 'No file part in the request'}), 400

    _file = request.files['file']

    height =  request.form.get('height')
    width = request.form.get('width')
    _format = request.form.get('format')

    converted_image = ImageConverter(_file.stream)

    converted_image_bytes, new_image_name = converted_image.get_converted_image(
        new_image_name="dummy_image_name",
        height=height,
        width=width,
        _format= _format
    )
    encoded_string = base64.b64encode(converted_image_bytes).decode('utf-8')

    return jsonify({'image_data': encoded_string, "type": "image/"+ _format.lower()})

@app.route('/', methods=['POST'])
def index_post():
    link = request.form['text']

    return jsonify({"data": YouTubeDownloader(link).get_video_download_data()})

if __name__ == '__main__':
    app.run(debug=True)
