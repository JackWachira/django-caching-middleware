from rest_framework import mixins, viewsets

from ..models import Author, Book, Publisher
from .serializers import AuthorSerializer, BookSerializer, PublisherSerializer


class BooksViewSet(mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = Book.objects.filter()
    serializer_class = BookSerializer


class AuthorsViewSet(mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    queryset = Author.objects.filter()
    serializer_class = AuthorSerializer


class PublishersViewSet(mixins.RetrieveModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    queryset = Publisher.objects.filter()
    serializer_class = PublisherSerializer
