from django.contrib import admin
from django.urls import path,include
from kishan.views import *

urlpatterns = [
    path("profile/",profile,name="profile"),
    path("",profile,name="profile"),
    path("profile/send_msg",send_msg,name="send_msg"),
]
