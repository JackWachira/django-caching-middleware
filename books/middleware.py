from django.conf import settings
from django.core.cache import caches
from django.http import JsonResponse
from rest_framework import status


class UrlCacheMiddleware:
    """
    Checks if request url matches urls to be cached.
    If match, returns cached page if cache exists else,
    caches page and returns reponse.
    If no match, it returns the page as is.
    """

    def __init__(self, get_response):
        self.get_response = get_response
        self.cache = caches[settings.CACHE_KEY]

    def __call__(self, request):
        cache_url = next((
            item for item in settings.CACHE_URLS if item["URL"] == request.path), None)
        if cache_url:
            try:
                timeout = int(cache_url['TIMEOUT'])
            except ValueError:
                return JsonResponse({'error': 'Set the timeout as a string representing number of seconds'}, status=status.HTTP_400_BAD_REQUEST)
            url = cache_url['URL']

            cached_response = self.cache.get(url)
            if cached_response:
                return cached_response
            else:
                response = self.get_response(request)
                if response.status_code == 200:
                    self.cache.set(url, response, timeout)
                return response

        response = self.get_response(request)
        return response
