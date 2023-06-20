from django.shortcuts import render
from .models import Attributes
from django.contrib.auth.models import User, auth
# Create your views here.



# Create your views here.
def mystock(request):
    atts= Attributes.objects.all()
    current_user = request.user
    seller_attributes = Attributes.objects.filter(sellername=current_user.username)
    # get authenticated user
    # filter out atts where an item in atts has same username as authenticated users.
    return render(request, "mystock.html",{"seller_attributes": seller_attributes})

