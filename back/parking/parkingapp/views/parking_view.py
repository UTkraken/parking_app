from rest_framework import viewsets

from ..models import Parking
from ..serializers.parking_serializer import ParkingSerializer


class ParkingViewSet(viewsets.ModelViewSet):
    serializer_class = ParkingSerializer
    queryset = Parking.objects.all()