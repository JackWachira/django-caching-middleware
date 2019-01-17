from django.conf.urls import include, url
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'books', views.BooksViewSet, base_name='books')
router.register(r'authors', views.AuthorsViewSet, base_name='authors')
router.register(r'publishers', views.PublishersViewSet, base_name='publishers')

urlpatterns = [
    url(r'^', include(router.urls)),
]
