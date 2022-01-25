# -----------------------------------------------------------
# An URL shortener API in Python
#
# (C) 2022 Sándor Daróczi, Munich, Germany
# -----------------------------------------------------------

from flask import Flask, request
from url_shortener import UrlShortener
from utils import is_url, error_to_json

import json

# creating Flask app
app = Flask(__name__)

# creating UrlShortener instance
urlShortener = UrlShortener()
base_url = urlShortener.base_url


# Defining what will happen on the main route
@app.route('/')
def home():
    return "Hey! This is an URL shortener service." \
           "To shorten an URL given by the string url_string, go to ./encode?url=url_string. Example:" \
           "http://127.0.0.1:7777/encode?url=https://wikipedia.org."



# Defining the encode endpoint
@app.route('/encode', methods=['GET'])
def api_encode():
    if 'url' not in request.args:
        return error_to_json("Error. No URL argument found.")
    long_url = request.args['url']
    if not is_url(long_url):
        return error_to_json("Error. The given string is not a valid URL.")

    encoder_response = urlShortener.encode(long_url)
    return encoder_response



# Defining the decode endpoint
@app.route('/decode', methods=['GET'])
def api_decode():
    if 'url' not in request.args:
        return error_to_json("Error. No URL argument found.")
    short_url = request.args['url']
    if not short_url.startswith(base_url):
        return error_to_json(f"Error. The URL must start with {base_url}")

    decoder_response = urlShortener.decode(short_url)
    return decoder_response



if __name__ == "__main__":
    app.run(port=7777, debug=True)
