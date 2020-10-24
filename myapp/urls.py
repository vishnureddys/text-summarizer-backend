from django.contrib import admin
from django.urls import path
from .views import show_form
#from .views import home_view, successView

urlpatterns = [
    path('home/', show_form, name='home'),
    #path('success/', successView, name='success'),
]