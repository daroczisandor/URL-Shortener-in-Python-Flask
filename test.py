import unittest
from url_shortener import UrlShortener
from utils import is_url

urls = [
    "https://wikipedia.org",
    "http://wikipedia.org",
    "http://youtube.com",
    "https://google.com",
    "https://www.spiegel.de/",
    "http://bild.de",
    "https://facebook.com",
    "http://magyarorszag.hu"
]

class TestUrlShortener(unittest.TestCase):

    def test_encode_len(self):
        """
        Tests if the length of the encoded URL is correct.
        """
        urlShortener = UrlShortener()

        for url in urls:
            encoder_response = urlShortener.encode(url)
            encoded_url = encoder_response['encoded_url']

            base_url = urlShortener.base_url
            num_chars = urlShortener.num_chars
            theoretical_length = len(base_url) + num_chars
            actual_length = len(encoded_url)

            assert(theoretical_length == actual_length)



    def test_encode_type(self):
        """
        Tests if the type of the encoded URL is a string.
        """
        urlShortener = UrlShortener()

        for url in urls:
            encoder_response = urlShortener.encode(url)
            encoded_url = encoder_response['encoded_url']

            assert(isinstance(encoded_url, str))



    def test_encode_different(self):
        """
        Tests whether different input urls yield different encodings.
        The probability of encoding collision is very low, so the encodings
        should practically always be different.
        """
        urlShortener = UrlShortener()
        encodings = []

        for url in urls:
            encoder_response = urlShortener.encode(url)
            encoded_url = encoder_response['encoded_url']
            assert (encoded_url not in encodings)
            encodings.append(encoded_url)



    def test_decode_valid(self):
        """
        Tests if the decoded URL is valid.
        """
        urlShortener = UrlShortener()

        for url in urls:
            encoder_response = urlShortener.encode(url)

        for short_url, long_url in urlShortener.short_to_long.items():
            assert(is_url(long_url))



    def test_url(self):
        """
        Tests if the different types URLS are valid or not
        """

        for url in urls:
            assert(is_url(url))

        assert(not is_url("www.google.com"))
        assert(not is_url(""))
        assert(not is_url("ttp://google.com"))
        assert(not is_url("http://google"))



if __name__ == '__main__':
    unittest.main()