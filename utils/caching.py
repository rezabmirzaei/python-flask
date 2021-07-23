from flask import request
from flask_caching import Cache

cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})


def cache_key_prefix():
    # Check headers first for api key
    api_key = request.headers.get('x-api-key')
    # If no api key provided in headers, check url request params
    api_key = request.args.get('key') if api_key is None else api_key
    cache_key_prefix = '' if api_key is None else api_key
    cache_key = f'{cache_key_prefix}_{request.url}'
    return cache_key
