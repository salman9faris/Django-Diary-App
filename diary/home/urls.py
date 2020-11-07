"""diary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from .views import home,register,signin,logout_request,diary,delete_diary,delete_conform,edit,search

urlpatterns = [
path('', home, name='home'),
path('register/', register, name='register'),
path('signin/', signin, name='signin'),
path('logout',logout_request,name='logout'),
path('diary',diary,name='diary'),
path('delete_diary/<int:id>',delete_diary,name='delete_diary'),
path('delete_conform/<int:id>',delete_conform,name='delete_conform'),
path('edit/<int:id>',edit,name='edit'),
path('search',search,name='search')
]
