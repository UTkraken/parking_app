from datetime import date

from rest_framework import serializers

from .floor_serializer import FloorSerializer
from .parking_serializer import ParkingSerializer
from .spot_serializer import SpotSerializer
from ..models import Reservation, Spot, Parking


class ReservationSerializer(serializers.ModelSerializer):
    parking_id = serializers.PrimaryKeyRelatedField(
        queryset=Parking.objects.all(),
        source='parking',
        write_only=True
    )
    date = serializers.DateField()
    parking = ParkingSerializer(read_only=True)
    floor = FloorSerializer(read_only=True)
    spot = SpotSerializer(read_only=True)

    class Meta:
        model = Reservation
        fields = [
            'id',
            'date',
            'parking',
            'parking_id',
            'floor',
            'spot',
        ]

    def create(self, validated_data):
        parking = validated_data['parking']
        date = validated_data['date']

        floor, spot = self.get_available_spot(parking, date)

        if not spot:
            raise serializers.ValidationError(f"No more spots available in {parking} at {date}")

        resa = Reservation.objects.create(
            date=date,
            parking=parking,
            floor=floor,
            spot=spot,
        )
        return resa

    def get_available_spot(self, parking, date):

        spots = Spot.objects.filter(floor__parking=parking)

        for spot in spots:
            reserverd = spot.reservations.filter(date=date).exists()
            if not reserverd:
                return (spot.floor, spot)

        return (None, None)