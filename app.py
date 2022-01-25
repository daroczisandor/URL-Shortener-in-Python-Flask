# -----------------------------------------------------------
# An URL shortener API in Python
#
# (C) 2022 Sándor Daróczi, Munich, Germany
# -----------------------------------------------------------

from flask import Flask, request
from url_shortener import UrlShortener
from utils import is_url

import json

# creating Flask app
app = Flask(__name__)

# creating UrlShortener instance
urlShortener = UrlShortener()



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
        return "Error. No URL found."
    long_url = request.args['url']
    if not is_url(long_url):
        return "Error. The given string is not a valid URL."

    encoded_url = urlShortener.encode(long_url)
    message = {
        'message': 'URL successfully encoded!',
        'encoded_url': encoded_url
    }
    message_json = json.loads(json.dumps(message))
    print("Jsonified message type: ", type(message_json))
    print("Jsonified message type: ", type(message_json))
    return message_json



if __name__ == "__main__":
    app.run(port=7777, debug=True)
