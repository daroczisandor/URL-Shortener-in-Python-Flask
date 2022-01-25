import string, random
from utils import error_to_json, url_to_json



class UrlShortener:
    def __init__(self, num_chars=5, base_url="http://127.0.0.1:7777/", max_it=1e5):
        """
        A UrlShortener class for generating an encoding for long URLs, and decoding short URLs.

        :param int num_chars: number of random characters used for encoding, default: 5
        :param string base_url: the URL of the homepage, default: "http://127.0.0.1:7777/"
        :param int max_it: maximum number of random tries to generate encoding, default: 100.000
        """
        self.num_chars = 5
        self.base_url = base_url
        self.max_it = max_it

        self.long_to_short = {}        # dictionary of all encoded links, grouped by long_url
        self.short_to_long = {}        # dictionary of all encoded links, grouped by short_url



    def encode(self, long_url):
        """
        The encoder method.

        :param string long_url: the url to be encoded
                                example: "https://wikipedia.org"
        :return: string short_url: the shortened url consisting of the base URL + self.num_chars random characters
                                   example: "http://127.0.0.1:7777/Ch5kf"
        """

        # if the long_url has already been encoded, return the shortened URL
        if long_url in self.long_to_short:
            return url_to_json({"message": "URL already encoded.",
                                "encoded_url": self.long_to_short[long_url]})

        # setting up a list of all lowercase and uppercase letters, as well as digits
        chars = string.ascii_letters + string.digits

        it = 0
        while(it < self.max_it):
            short_code = ''.join(random.choice(chars) for i in range(self.num_chars))     # generate encoding
            short_url = self.base_url + short_code                                        # append generated encoding to the base URL
            if short_url not in self.short_to_long:                                       # return the encoding if it has not already been used
                self.insert_encoding(short_url, long_url)                                 # insert the short-long URL pair into the dictionaries
                print("Long to short dict: ", self.long_to_short)
                print("Short to long dict: ", self.short_to_long)

                return url_to_json({"message": "Success! The input URL has been encoded.",
                                    "encoded_url": short_url})
            it += 1

        return error_to_json("Error. Couldn't encode the URL due to runtime issues. Try again later.")



    def decode(self, short_url):
        """
        The decoder method.

        :param string short_url: the URL to be decoded
                                 example: "http://127.0.0.1:7777/Ch5kf"
        :return: string long_url: the decoded URL
                                  example: "https://wikipedia.org"
        """

        # if the short_url has already been used to encode an URL, return the corresponding long URL
        if short_url in self.short_to_long:
            return url_to_json({"message": "Success! The input URL has been decoded.",
                                "decoded_url": self.short_to_long[short_url]})

        # else return an error message
        return error_to_json("Error. No long URL corresponds to the provided short URL.")



    def insert_encoding(self, short_url, long_url):
        """
        Inserting a short_url - long_url pair into both dictionaries

        :param string short_url
        :param string long_url
        """
        self.long_to_short[long_url] = short_url
        self.short_to_long[short_url] = long_url


# if __name__ == "__main__":
#     Encoder = Encoder()
#     Encoder.encode("322352")
