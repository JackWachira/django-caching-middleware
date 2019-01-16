from django.db import models

from .utils import get_uuid


class BaseModel(models.Model):
    """
    An abstract base class model that has a UUID primary key
    """
    id = models.UUIDField(primary_key=True, default=get_uuid, editable=False)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    modified_on = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True
