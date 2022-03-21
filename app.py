from flask import Flask,request
from main import gpt3
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])

def upload():

    link = request.get_json()
    url = link["url"]
    width = link["width"]
    height = link["height"]

    print(url)
    x = gpt3(url, width, height)
    return x

if __name__ == '__main__':
    app.run(debug=True)