from rest_framework import serializers

from ..models.spot import Spot


class SpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spot
        fields = [
            'id',
            'number',
            'floor',
        ]