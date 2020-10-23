from django.contrib import admin
from django.urls import path

from .views import home_view, successView

urlpatterns = [
    path('home/', home_view, name='home'),
    path('success/', successView, name='success'),
]