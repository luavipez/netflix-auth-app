# backend/urls.py
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
     path('user/*', views.RegisterView.as_view(), name='register'),
]