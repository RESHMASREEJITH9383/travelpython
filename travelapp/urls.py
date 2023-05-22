from .models import place
from django.urls import path
from django .shortcuts import render
from travelapp import views


urlpatterns = [
    path('', views.demo, name ='register'),
]
    # path('add/',views.addition,name='addition'),
    # path('division/',views.division,name='division'),
    # path('multiplication/',views.mutiplication,name='mutiplication'),
    #
