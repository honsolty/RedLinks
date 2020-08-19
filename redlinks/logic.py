import time
import json
import redis
from aiohttp import web
from views import post_link, get_link
from test import test_json
# from custom_errors import LinkError


def post(request=test_json['post']):
    try:
        post_link(request)
        response = {'status': 'ok'}
    except LinkError as error:
        response = {'status': 'failed', 'reason': "wrong address fromat", "error" : error}
    except KeyError as error:
        response = {'status': 'failed', 'reason': "parametr 'address' required", "error" : error}
    finally:
        return web.Response(text=json.dumps(response))


def get(request=test_json['get']):
    try:
        response = get_link(request)
    except ValueError as error:
        response = {'status': 'failed', 'reason': "wrong time format", "error" : error}
    except KeyError as error:
        response = {'status': 'failed', 'reason': "parameters 'from' or 'to' are missing", "error" : error}
    finally:
        return web.Response(text=json.dumps(response))
    