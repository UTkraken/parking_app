import uuid

from django.db import models


class Floor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.IntegerField()

    parking = models.ForeignKey(
        'Parking',
        on_delete=models.CASCADE,
        related_name='floors',
    )

    def __str__(self):
        return f'{self.number} - {self.parking}'