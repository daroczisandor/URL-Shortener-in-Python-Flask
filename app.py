# -----------------------------------------------------------
# An URL shortener API in Python
#
# (C) 2022 Sándor Daróczi, Munich, Germany
# -----------------------------------------------------------

from flask import Flask, request, jsonify
from url_shortener import UrlShortener
from utils import is_url

# creating Flask app
app = Flask(__name__)

# Defining what will happen on the main route
@app.route('/')
def hello_world():
    return "Hello World!"

# Defining the encode endpoint
@app.route('/encode', methods=['GET'])
def api_encode():

    if 'url' not in request.args:
        return "Error. No URL found."
    url = request.args['url']
    if not is_url(url):
        return "Error. The given string is not a valid URL."

    return "Success! Valid URL provided."

if __name__ == "__main__":
    app.run(port=7777, debug=True)
