from datetime import datetime

from rest_framework import serializers

from ..models import Parking, Spot, Reservation


class ParkingSerializer(serializers.ModelSerializer):
    floor_count = serializers.SerializerMethodField()
    spot_count = serializers.SerializerMethodField()
    available_spots_count = serializers.SerializerMethodField()

    class Meta:
        model = Parking
        fields = [
            'id',
            'name',
            'code',
            'floor_count',
            'spot_count',
            'available_spots_count',
        ]

    def get_floor_count(self, obj):
        return obj.floors.count()

    def get_spot_count(self, obj):
        return sum(floor.spots.count() for floor in obj.floors.all())

    def get_available_spots_count(self, obj):
        date = self.context.get('date')

        if not date:
            date = datetime.now()

        all_spots = Spot.objects.filter(floor__parking=obj)

        reserved_spots = Reservation.objects.filter(parking=obj, date=date).values_list('spot', flat=True)

        available_spots = all_spots.exclude(id__in=reserved_spots)

        return available_spots.count()