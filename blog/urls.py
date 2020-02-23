from django.contrib import admin
from django.urls import path, include
from . import views
from . views import (
    Home,
    detail,
)

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('detail/<slug:slug>/', detail.as_view(), name='detail'),
    path('kontak/', views.kontak, name='kontak'),
]