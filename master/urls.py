"""master URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'Condingtenetz Admin'

'''
This is the entry point of the service from here service will be routed to individual apps based on the routing
This was created by default when first project was created. It is the first django restframework project created. 
It has some important files like Setting.py and any new installed app is added to the setting file ( like api, vehicle, coreapi)
'''
urlpatterns = [   
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/vehicle/', include('vehicle.urls')),
    
]
