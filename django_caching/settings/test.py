from .base import *

DEBUG = True
CACHE_KEY = 'test'

CACHES = {
    CACHE_KEY: {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

CACHE_URLS = [
    {
        'URL': '/api/v1/books/',
        'TIMEOUT': '30'
    }
]

NOSE_ARGS = ['--nocapture',
             '--nologcapture', ]
