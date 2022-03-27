from flask import Flask
from analyze import get_data

app = Flask(__name__)

@app.route('/analyze/<lon>/<lat>', methods = ['POST', 'GET'])
def analyze(lon, lat):
    get_data(lom, lat)
    return 'Hello, World!'