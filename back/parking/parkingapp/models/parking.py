import uuid

from django.db import models

class Parking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return f'{self.name} - {self.code}'