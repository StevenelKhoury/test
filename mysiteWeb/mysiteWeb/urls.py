"""mysiteWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from App1.views import *
from App1.templates import *
from rest_framework import routers
#from django.conf.urls import patterns, include, url


#router = routers.DefaultRouter()
#router.register(r'product', ProductViewSet)
#router.register(r'supplier', SupplierViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/',addUti,name='ajout_Utilisateur'),
    #url(r'^api/', include(router.urls)),
]

