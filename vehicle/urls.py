from django.urls import path
from .import views

urlpatterns = [    
     path('<int:pk>/', views.vehicle_detail_view),
     path('', views.vehicle_list_create_view),
     path('update/<int:pk>/', views.vehicle_update_view),
     path('delete/<int:pk>/', views.vehicle_delete_view),
]
