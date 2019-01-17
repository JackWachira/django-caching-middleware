from core.models import BaseModel
from django.db import models


class Book(BaseModel):
    code = models.IntegerField(unique=True)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
