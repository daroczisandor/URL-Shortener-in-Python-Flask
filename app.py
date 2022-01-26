# -----------------------------------------------------------
# An URL shortener API in Python
#
# (C) 2022 Sándor Daróczi, Munich, Germany
# -----------------------------------------------------------

from flask import Flask, request, render_template
from url_shortener import UrlShortener
from utils import is_url, error_to_json



# creating Flask app
app = Flask(__name__)

# creating UrlShortener instance
urlShortener = UrlShortener()
base_url = urlShortener.base_url


# Defining what will happen on the home page
@app.route('/')
def home():
    return render_template('home.html')



@app.route('/encode', methods=['GET'])
def api_encode():
    """
    Encode endpoint that looks for a long_url provided as an 'url' argument,
    encodes it via an UrlShortener class instance, and returns the encoded
    URL together with a message as JSON
    If no url argument was found, or the long_url is invalid, it returns
    an error message.

    :return: the encoded link as a JSON of the form {'message': message,
                                                     'encoded_url': encoded_url},
             or an error message of the form {'message': error_message}
    """

    # if no url argument was given, return error
    if 'url' not in request.args:
        return error_to_json("Error. No URL argument found.")

    long_url = request.args['url']

    # if the URL is not valid, return error
    if not is_url(long_url):
        return error_to_json("Error. The given string is not a valid URL.")

    # return encoded url as JSON
    encoder_response = urlShortener.encode(long_url)
    return encoder_response



@app.route('/decode', methods=['GET'])
def api_decode():
    """
    Decode endpoint that gets a short_url provided as an 'url' argument,
    looks up the long_url that has been encoded to get the short_url, and
    then return the long_url as a JSON.
    If no corresponding long_url exists, it returns an error message.

    :return: the encoded link as a JSON of the form {'message': message,
                                                     'decoded_url': decoded_url},
             or an error message of the form {'message': error_message}
    """

    # if no url argument was given, return error
    if 'url' not in request.args:
        return error_to_json("Error. No URL argument found.")
    short_url = request.args['url']

    # if the short URL does not start with "http://127.0.0.1:7777/", return error
    if not short_url.startswith(base_url):
        return error_to_json(f"Error. The URL must start with {base_url}")

    # return decoded URL as JSON
    decoder_response = urlShortener.decode(short_url)
    return decoder_response



if __name__ == "__main__":
    app.run(port=7777, debug=True)
