from utils import get_api_key
from flask import request, session
from flask_caching import Cache

cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})


def cache_key_prefix():
    api_key = get_api_key()
    cache_key_prefix = '' if api_key is None else api_key
    cache_key = f'{cache_key_prefix}_{request.url}'
    return cache_key
