from django.conf.urls import include, url

urlpatterns = [
    url(r'library/', include('books.api.urls')),
]
