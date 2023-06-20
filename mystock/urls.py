from django.urls import path
from . import views

urlpatterns=[path("mystock",views.mystock,name="mystock")
             ]