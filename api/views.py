from django.http import JsonResponse
from django.forms.models import model_to_dict
from .models import Enquiry
from .serializers import EnquirySerializer

from rest_framework import generics, permissions, authentication
from vehicle.permissions import StaffEditorPermission

from vehicle.models import Vehicle
from vehicle.serializers import VehicleSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(["POST"])
def api_home(request, *args, **kwargs):        
    serializer = VehicleSerializer(data=request.data)
    if serializer.is_valid(): 
        data = serializer.save()       
        print(data)       
        
        return Response(serializer.data)
    
@api_view(["POST"])
def api_enquiry(request, *args, **kwargs):        
    serializer = EnquirySerializer(data=request.data)
    if serializer.is_valid(): 
        data = serializer.save()
        print(data)
        
        return Response(serializer.data)    
    
    # This is generic API view where declarative syntax does all the work
    # Create keyword specifies that it is a POST requrest 
    # View, detail view, Add new
class EnquiryCreateAPIView(generics.CreateAPIView):
    queryset = Enquiry.objects.all()
    serializer_class = EnquirySerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [StaffEditorPermission]

