from rest_framework import serializers

from .models import Vehicle

class VehicleSerializer(serializers.ModelSerializer):
    # my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Vehicle
        fields = [
            'title',
            'model',
            'price',
            'average',
            # 'my_discount',
        ]        
        