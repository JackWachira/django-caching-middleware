from rest_framework import serializers

from ..models import Author, Book, Publisher


class BookSerializer(serializers.ModelSerializer):
    """Book Model Serializer. """
    class Meta:
        model = Book
        fields = ('__all__')


class AuthorSerializer(serializers.ModelSerializer):
    """Author Model Serializer. """
    class Meta:
        model = Author
        fields = ('__all__')


class PublisherSerializer(serializers.ModelSerializer):
    """Author Model Serializer. """
    class Meta:
        model = Publisher
        fields = ('__all__')
