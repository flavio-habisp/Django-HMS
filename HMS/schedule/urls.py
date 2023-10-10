
from django.contrib import admin
from django.urls import path, include
from accounts.views import *
from room.views import *
from hotel.views import *
from . import views
urlpatterns = [
    path("", views.week, name="schedule"),
    path("next/<str:day>", views.week, name="schedule"),
    path("previous/<str:day>", views.week, name="schedule"),
    path("attendance", views.attendance, name="attendance"),
    path("attendance/next/<str:day>", views.attendance, name="attendance"),
    path("attendance/previous/<str:day>", views.attendance, name="attendance"),
]