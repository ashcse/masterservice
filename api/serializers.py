from rest_framework import serializers

from .models import Enquiry

class EnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Enquiry
        fields = [
            'email_addr',
            'description',
            'created_at'
        ]