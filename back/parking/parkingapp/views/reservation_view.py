from rest_framework import viewsets

from ..models import Reservation
from ..serializers.reservation_serializer import ReservationSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    serializer_class = ReservationSerializer
    queryset = Reservation.objects.all()
