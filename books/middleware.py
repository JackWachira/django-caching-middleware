import re

regex_http_ = re.compile(r'^HTTP_AGENT$')


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
        print(request.__dict__)
        response = self.get_response(request)
        return response
