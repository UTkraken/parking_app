import uuid

from django.db import models


class Reservation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField(auto_now=False, auto_now_add=False)

    parking = models.ForeignKey(
        'Parking',
        on_delete=models.CASCADE,
        related_name='reservations'
    )

    floor = models.ForeignKey(
        'Floor',
        on_delete=models.CASCADE,
        related_name='reservations',
        null=True
    )

    spot = models.ForeignKey(
        'Spot',
        on_delete=models.CASCADE,
        related_name='reservations',
        null=True
    )

    def __str__(self):
        return f'{self.date} - {self.parking} - {self.floor} - {self.spot}'

    class Meta:
        unique_together = ('date', 'parking', 'floor', 'spot')