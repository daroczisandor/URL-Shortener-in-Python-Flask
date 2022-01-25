import string, random

# An URL Shortener class used to encode and decode url's.
class UrlShortener:
    def __init__(self, num_chars=5, base_url="http://127.0.0.1:7777/", max_it=1e5):
        """

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
        :return: string short_url: the shortened url consisting of self.num_chars characters
        """

        # if the long_url has already been encoded, return the shortened URL
        if long_url in self.long_to_short:
            return self.long_to_short[long_url]

        # generate encoding by grouping together num_chars many random characters
        chars = string.ascii_letters + string.digits

        it = 0
        while(it < self.max_it):
            short_code = ''.join(random.choice(chars) for i in range(self.num_chars))      # generate encoding
            short_url = self.base_url + short_code                                         # append generated encoding to the base URL
            if short_url not in self.short_to_long:
                self.insert_encoding(short_url, long_url)
                print("Long to short dict: ", self.long_to_short)
                print("Short to long dict: ", self.short_to_long)

                return short_url
            it += 1

        return "Error, couldn't encode the URL. Try again."



    def decode(self, short_url):
        """
        The decoder method.

        :param string short_url: the URL to be decoded
        :return: string long_url: the decoded URL
        """

        # if the short_url has already been used to encode an URL, return the corresponding long URL
        if short_url in self.short_to_long:
            return self.short_to_long[short_url]

        # else return an error message
        return "Error, no URL corresponds to the given short URL."



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
