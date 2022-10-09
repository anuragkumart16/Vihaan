from django.shortcuts import render
from Buyer.models import Buyer_table
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method=="POST":
        name=request.POST.get('buyer_name')
        phone=request.POST.get('buyer_phone')
        adhaar=request.POST.get('buyer_adhaar')
        password=request.POST.get('buyer_pass1')

        Buyer=Buyer_table(buyer_name=name,buyer_phone=phone,buyer_adhaar=adhaar,buyer_pass1=password)
        Buyer.save()
        messages.success(request,'Successfully Signed Up')
    return render(request,"buyer.html")
