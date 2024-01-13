from django.contrib import admin
from django.urls import path,include
from kishan.views import *

urlpatterns = [
    path("profile/",profile,name="profile"),
]
