from django.contrib import admin
from django.urls import path
from platzigram import views

urlpatterns = [
    path('hello', views.hello),
    path('hi', views.hi)
]
