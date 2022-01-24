import string, random

class UrlShortener:
    def __init__(self, num_chars=5):
        """

        :param int num_chars: the length of the encoded urls
        :var dict data: dictionary of the long - short url pairs
        """
        self.num_chars = 5
        self.data = {}
        pass

    def encode(self, long_url):
        """

        :param string long_url: the url to be shortened
        :return: string short_url: the shortened url
        """
        chars = string.ascii_letters + string.digits
        short = ''.join(random.choice(chars) for i in range(self.num_chars))

        return short


    def decode(self):
        pass

if __name__ == "__main__":
    Encoder = Encoder()
    Encoder.encode("322352")
