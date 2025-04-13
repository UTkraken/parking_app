from rest_framework import viewsets

from ..models import Floor
from ..serializers.floor_serializer import FloorSerializer


class FloorViewSet(viewsets.ModelViewSet):
    serializer_class = FloorSerializer
    queryset = Floor.objects.all()