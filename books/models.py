from core.models import BaseModel
from django.db import models


class Author(BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title


class Book(BaseModel):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
