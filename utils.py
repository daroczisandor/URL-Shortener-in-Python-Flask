import validators
from validators import ValidationFailure

import json

# checks if a given string is a valid URL
def is_url(url_string):
    """

    :param string url_string: the URL to be validated
    :return: bool valid: True if url_string is a valid URL
                         False if url_string is not a valid URL
    """
    valid = validators.url(url_string)
    if isinstance(valid, ValidationFailure):
        return False

    return True



def error_to_json(error_message, return_json=True):
    message = {
        'message': error_message
    }

    if (return_json):
        return json.loads(json.dumps(message))
    return message



def url_to_json(message, return_json=True):
    if (return_json):
        return json.loads(json.dumps(message))
    return message


# if __name__ == "__main__":
#     url = "https://wikipedia.org"
#     print(is_url(url))