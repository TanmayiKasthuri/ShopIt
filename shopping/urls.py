from django.urls import path
from . import views

urlpatterns=[path("",views.index,name="index"),
             path("index",views.index,name="index"), #path("index-route",views.index-function,name="index"), mystock/index->in mystock module, route function
             path("contact",views.contact,name="contact"),
             path("shoplist",views.shoplist,name="shoplist"),
             path("about",views.about,name="about")]