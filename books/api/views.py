from rest_framework import mixins, viewsets

from ..models import Book
from .serializers import BookSerializer


class BooksViewSet(mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = Book.objects.filter()
    serializer_class = BookSerializer
