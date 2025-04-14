from rest_framework import viewsets, status
from rest_framework.response import Response

from ..models import Parking
from ..serializers.parking_serializer import ParkingSerializer


class ParkingViewSet(viewsets.ModelViewSet):
    serializer_class = ParkingSerializer
    queryset = Parking.objects.all()


    def list(self, request, *args, **kwargs):
        date = request.query_params.get('date')
        parkings = Parking.objects.all()
        serializer = self.get_serializer(parkings, many=True, context={'date': date})

        return Response(serializer.data)