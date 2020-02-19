from django.contrib import admin
from django.urls import path, include
from . import views
from . views import (
    Home,
)

urlpatterns = [
    path('home', Home.as_view(), name='home'),
]