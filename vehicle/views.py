from rest_framework import generics, permissions, authentication
from .models import Vehicle
from .serializers import VehicleSerializer
from .permissions import StaffEditorPermission


'''
These are generic views which are used with authentication and authorization logic for simple crud operations for vehicle objects.
For any complex business logic move the logic classes to separate service classes and keep the views thin
'''

'''Detail view which will use pk as parameter and returns details'''
class VehicleDetailAPIView(generics.RetrieveAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
vehicle_detail_view = VehicleDetailAPIView.as_view()


'''Handles POST and GET both for vehicle listing and vehicle addition'''
class VehicleListCreateAPIView(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [StaffEditorPermission]    
vehicle_list_create_view = VehicleListCreateAPIView.as_view()


'''Update view'''
class VehicleUpdateAPIView(generics.UpdateAPIView):
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [StaffEditorPermission]
    
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    lookup_field = 'pk'
    
    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.model:
            instance.model = instance.title
        
    
vehicle_update_view = VehicleUpdateAPIView.as_view()


'''Delete view'''
class VehicleDeleteAPIView(generics.DestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    lookup_field = 'pk'
    
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)
    
    
        
    
vehicle_delete_view = VehicleDeleteAPIView.as_view()

