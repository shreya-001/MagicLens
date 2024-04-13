from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin
import util

app = Flask(__name__)
CORS(app, supports_credentials=True) 

# Default Route
@app.route("/")
def home():
    return render_template("app.html")


@app.route('/classify_image', methods=['GET', 'POST'])
def classify_image():
    image_data = request.form['image_data']

    response = jsonify(util.classify_image(image_data))

    # response.headers.add('Access-Control-Allow-Origin', 'localhost')

    return response

if __name__ == "__main__":
    util.load_saved_artifacts()
    app.run(port=5000)
