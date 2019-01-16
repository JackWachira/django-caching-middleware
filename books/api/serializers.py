from rest_framework import serializers

from ..models import Book


class BookSerializer(serializers.ModelSerializer):
    """Book Model Serializer. """
    class Meta:
        model = Book
        fields = ('__all__')
