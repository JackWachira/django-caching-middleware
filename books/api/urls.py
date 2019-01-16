from django.conf.urls import include, url
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'', views.BooksViewSet, base_name='books')

urlpatterns = [
    url(r'^', include(router.urls)),
]
