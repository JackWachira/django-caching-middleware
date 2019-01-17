from .base import *

DEBUG = True
CACHE_KEY = 'default'

CACHES = {
    CACHE_KEY: {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

CACHE_URLS = [
    {
        'URL': '/api/v1/library/authors/',
        'TIMEOUT': '60'
    },
    {
        'URL': '/api/v1/library/books/',
        'TIMEOUT': '30'
    }
    {
        'URL': '/api/v1/library/publishers/',
        'TIMEOUT': '300'
    }
]
