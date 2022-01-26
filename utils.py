import validators, json
from validators import ValidationFailure



def is_url(url_string):
    """
    Checks if a given string is a valid URL.

    :param string url_string: the URL to be validated
    :return: bool valid: True if url_string is a valid URL
                         False if url_string is not a valid URL
    """

    # Create validators instance
    valid = validators.url(url_string)
    if isinstance(valid, ValidationFailure):
        return False

    return True




def error_to_json(error_message):
    """
    A helper function to convert an error message to a JSON dict

    :param string error_message: the error message to be converted
    :return: JSON message of the form {'message': error_message,
                                       'status': 'error'}

    """

    message = {
        'message': error_message,
        'status': 'error'
    }
    return json.loads(json.dumps(message))




def url_to_json(message):
    """
    A helper function to convert a message and a URL to JSON

    :param dict message: a dictionary of the form {'message': input_message,
                                                   'url': input_url}
    :return: the message converted to JSON
    """

    return json.loads(json.dumps(message))