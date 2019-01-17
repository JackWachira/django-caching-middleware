import re

from django.conf import settings
from django.core.cache import cache
from django.urls import resolve


class UrlCacheMiddleware:
    """
    Checks if request url matches urls to be cached.
    If match, returns cached page if cache exists else,
    caches page and returns reponse.
    If no match, it returns the page as is.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        cache_url = next((
            item for item in settings.CACHE_URLS if item["URL"] == request.path), None)
        timeout = int(cache_url['TIMEOUT'])
        url = cache_url['URL']

        cached_response = cache.get(url)
        if cached_response:
            return cached_response
        response = self.get_response(request)
        cache.set(url, response, timeout)
        return response
