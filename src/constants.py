import os

# ROOT Project Path
CURRENT_DIR = 'src'
ROOT_DIR = os.path.dirname(os.path.abspath(__file__)).replace(CURRENT_DIR, '')
ENV_TEST_DIR = os.path.join(ROOT_DIR, '.env.test')


# API
V1 = '/v1'
BASE_URI_V1 = '/api' + V1
BARCODE_PARAM = '/<string:barcode>'
URI_PRODUCTS = '/products'
URI_PURCHASES = '/purchases'

JSON_MIME_TYPE = 'application/json'
ID = 'id'
HREF = 'href'

# HTTP Response Codes
CREATED = 201
OK = 200
CONFLICT = 409
NOT_FOUND = 404
SERVER_ERROR = 500

# HTTP Methods
GET = 'GET'
POST = 'POST'
PUT = 'PUT'
DELETE = 'DELETE'

