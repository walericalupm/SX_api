from flask import json
from app import app
from constants import *


def base_response_body(resource_id, resource_uri):
    response_body = {
        ID: resource_id,
        HREF: resource_uri + '/' + resource_id
    }
    return response_body


def resource_response_object(resource):
    return


def base_response_object(response_body, code):
    response = app.response_class(
        response=json.dumps(response_body),
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
    return base_response_object(resource, OK)


def api_error_response(code):
    if code is SERVER_ERROR:
        message = 'Server Error'
    if code is NOT_FOUND:
        message = 'Resource Not Found'

    response_body = {"message": message}
    return base_response_object(response_body, code)
