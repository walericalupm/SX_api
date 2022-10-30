import json
from flask import jsonify
from src.app import app
from src.constants import *


def base_response_body(resource_id, resource_uri):
    response_body = {
        ID: resource_id,
        HREF: resource_uri + '/' + resource_id
    }
    return json.dumps(response_body)


def base_response_object(response_body, code):
    response = app.response_class(
        response=response_body,
        status=code,
        mimetype=JSON_MIME_TYPE
    )
    return response


def api_response(resource_id, resource_uri, code):
    if resource_id is None:
        response = base_response_object(None, OK)
    else:
        response_body = base_response_body(resource_id, resource_uri)
        response = base_response_object(response_body, code)
    return response


def api_resource_response(resource):
    return jsonify(resource)


def api_error_response(code):
    if code is NOT_FOUND:
        message = 'Resource Not Found'
    else:
        message = 'Server Error'
    response_body = {"message": message}
    return base_response_object(response_body, code)
