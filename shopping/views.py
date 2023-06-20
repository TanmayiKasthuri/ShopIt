from django.shortcuts import render
from .models import Attributes


# Create your views here.
def index(request):
    atts= Attributes.objects.all()
    return render(request, "index.html",{'atts':atts})
def contact(request):
    return render(request, "contact.html")
def shoplist(request):
    atts= Attributes.objects.all()
    return render(request,"shoplist.html",{'atts':atts})
def about(request):
    return render(request, "about.html")

