import requests
from flask_cors import CORS, cross_origin
from resolvers.main_resolver import query
from resolvers.youtube_downloader import YouTubeDownloader
from schemas.type_definitions import type_definitions
from ariadne import make_executable_schema, graphql_sync
from flask import Flask, jsonify, request, render_template

app = Flask(__name__, template_folder="pages/templates")
CORS(app, supports_credentials=True, allow_headers=['Content-Type', 'Authorization'],)

ALLOWED_ORIGINS = ['*']
# from ariadne.constants import PLAYGROUND_HTML

# Create executable schema
schema = make_executable_schema(type_definitions, query)

@app.route("/graphql", methods=["POST"])
@cross_origin(origins='*')
def graphql_server():
    data = request.get_json()

    success, result = graphql_sync(
        schema, data, context_value={"request": request})
    status_code = 200 if success else 400
    return jsonify(result), status_code

@app.route('/', methods=['GET'])
def index():
    # link = request.form['text']

    # response = requests.get(
    #     "https://rr2---sn-8vq5jvh15-2gts.googlevideo.com/videoplayback?expire=1730858497&ei=oXkqZ5-BNIncp-oP4bWIwQo&ip=105.245.101.45&id=o-AEEcacDXzTho1rrI934yki7IkNqUbAO1MpAE1JJdzE_l&itag=399&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&met=1730836897%2C&mh=1M&mm=31%2C29&mn=sn-8vq5jvh15-2gts%2Csn-8vq5jvh15-wocl&ms=au%2Crdu&mv=m&mvi=2&pl=18&rms=au%2Cau&initcwndbps=270000&vprv=1&svpuc=1&mime=video%2Fmp4&rqh=1&gir=yes&clen=3804408&dur=15.081&lmt=1728750994084800&mt=1730836414&fvip=3&keepalive=yes&fexp=51312688%2C51326932&c=IOS&txp=543C434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cvprv%2Csvpuc%2Cmime%2Crqh%2Cgir%2Cclen%2Cdur%2Clmt&sig=AJfQdSswRQIgXLE4uJCpKphQ4wA07AQPIwoPt2LIJuQxMqm-X9h2Qu0CIQDlRErjLX3NyuGAsQv_Cpf9sWS8K-jPrnSIFgpdM8Sj_Q%3D%3D&lsparams=met%2Cmh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Crms%2Cinitcwndbps&lsig=ACJ0pHgwRQIgCG-oNhBUu_290CyHi-PmoHlzEvxuDVPyRgwlMgank0wCIQDwJc78ri5fLRFphJs0Yg_bmOAFjj69lApl0_Z7MrKJBA%3D%3D",
    #     stream=True)
    # response.raise_for_status()
    #
    # content_type = response.headers.get('Content-Type')
    # print(content_type)
    # # Create a response object
    # response_obj = make_response(response.content, 200)
    #
    # # Set Content-Disposition and Content-Type headers
    # response_obj.headers.set('Content-Disposition', f'attachment; filename="{"filename.mp4"}"')
    # response_obj.headers.set('Content-Type', content_type)
    # return response_obj
    return render_template("index.html")
@app.route('/', methods=['POST'])
def index_post():
    link = request.form['text']
    #
    # response = requests.get(
    #     "https://rr2---sn-8vq5jvh15-2gts.googlevideo.com/videoplayback?expire=1730858497&ei=oXkqZ5-BNIncp-oP4bWIwQo&ip=105.245.101.45&id=o-AEEcacDXzTho1rrI934yki7IkNqUbAO1MpAE1JJdzE_l&itag=399&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&met=1730836897%2C&mh=1M&mm=31%2C29&mn=sn-8vq5jvh15-2gts%2Csn-8vq5jvh15-wocl&ms=au%2Crdu&mv=m&mvi=2&pl=18&rms=au%2Cau&initcwndbps=270000&vprv=1&svpuc=1&mime=video%2Fmp4&rqh=1&gir=yes&clen=3804408&dur=15.081&lmt=1728750994084800&mt=1730836414&fvip=3&keepalive=yes&fexp=51312688%2C51326932&c=IOS&txp=543C434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cvprv%2Csvpuc%2Cmime%2Crqh%2Cgir%2Cclen%2Cdur%2Clmt&sig=AJfQdSswRQIgXLE4uJCpKphQ4wA07AQPIwoPt2LIJuQxMqm-X9h2Qu0CIQDlRErjLX3NyuGAsQv_Cpf9sWS8K-jPrnSIFgpdM8Sj_Q%3D%3D&lsparams=met%2Cmh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Crms%2Cinitcwndbps&lsig=ACJ0pHgwRQIgCG-oNhBUu_290CyHi-PmoHlzEvxuDVPyRgwlMgank0wCIQDwJc78ri5fLRFphJs0Yg_bmOAFjj69lApl0_Z7MrKJBA%3D%3D",
    #     stream=True)
    # response.raise_for_status()
    #
    # content_type = response.headers.get('Content-Type')
    #
    # # Create a response object
    # response_obj = make_response(response.content, 200)
    #
    # # Set Content-Disposition and Content-Type headers
    # response_obj.headers.set('Content-Disposition', f'attachment; filename="{"filename.mp4"}"')
    # response_obj.headers.set('Content-Type', content_type)
    # return  response_obj
    return jsonify({"data": YouTubeDownloader(link).get_video_download_data()})

if __name__ == '__main__':
    app.run(debug=True)
