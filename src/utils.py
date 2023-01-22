from src.constants import JSON_MIME_TYPE, NOT_FOUND, MESSAGE, NOT_FOUND_MESSAGE, SERVER_ERROR_MESSAGE
from src.app import app
from flask import json


def base_response_object(response_body, code):
    response = app.response_class(
        response=response_body,
        status=code,
        mimetype=JSON_MIME_TYPE
    )
    return response


def api_error_response(code, message=None):
    if message is None:
        if code is NOT_FOUND:
            message = NOT_FOUND_MESSAGE
        else:
            message = SERVER_ERROR_MESSAGE
    response_body = json.dumps({MESSAGE: message})
    return base_response_object(response_body, code)


def api_resource_response(response_body, code):
    return base_response_object(json.dumps(response_body), code)
