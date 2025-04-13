import uuid

from django.db import models


class Spot(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.IntegerField()

    floor = models.ForeignKey(
        'Floor',
        on_delete=models.CASCADE,
        related_name='spots',
    )

    def __str__(self):
        return f'{self.number} - {self.floor}'