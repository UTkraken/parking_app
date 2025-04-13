from rest_framework import serializers

from ..models import Parking


class ParkingSerializer(serializers.ModelSerializer):
    floor_count = serializers.SerializerMethodField()
    spot_count = serializers.SerializerMethodField()

    class Meta:
        model = Parking
        fields = [
            'id',
            'name',
            'code',
            'floor_count',
            'spot_count',
        ]

    def get_floor_count(self, obj):
        return obj.floors.count()

    def get_spot_count(self, obj):
        return sum(floor.spots.count() for floor in obj.floors.all())