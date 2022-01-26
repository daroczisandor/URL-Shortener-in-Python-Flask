import validators, json
from validators import ValidationFailure



# checks if a given string is a valid URL
def is_url(url_string):
    """

    :param string url_string: the URL to be validated
    :return: bool valid: True if url_string is a valid URL
                         False if url_string is not a valid URL
    """

    # Create validators in
    valid = validators.url(url_string)
    if isinstance(valid, ValidationFailure):
        return False

    return True




def error_to_json(error_message):
    """
    A helper function to convert an error message to a JSON dict

    :param string error_message: the error message to be converted
    :param bool return_json: whether the output should be json dict, or a python dict
    :return: the message converted to json
    """

    message = {
        'message': error_message
    }
    return json.loads(json.dumps(message))




def url_to_json(message):
    """
    A helper function to convert a message and a URL to JSON

    :param dict message: a dictionary of the form
                         {'message': input_message,
                          'url': input_url}
    :param return_json: whether the output should be json dict, or a python dict
    :return: the message converted to json
    """

    return json.loads(json.dumps(message))


# if __name__ == "__main__":
#     url = "https://wikipedia.org"
#     print(is_url(url))