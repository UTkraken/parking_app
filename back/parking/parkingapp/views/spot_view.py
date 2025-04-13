from rest_framework import viewsets

from ..models import Spot
from ..serializers.spot_serializer import SpotSerializer


class SpotViewSet(viewsets.ModelViewSet):
    serializer_class = SpotSerializer
    queryset = Spot.objects.all()
