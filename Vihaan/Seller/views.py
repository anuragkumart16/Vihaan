from django.shortcuts import render
from Seller.models import Seller_table
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method=="POST":
        # form = Seller_table(request.POST, request.FILES)
        name=request.POST.get('seller_name')
        phone=request.POST.get('seller_phone')
        raw=request.POST.get('seller_raw')
        price=request.POST.get('seller_price')
        discription=request.POST.get('desc')
        image=request.POST.get('img')
        Seller=Seller_table(seller_name=name,seller_phone=phone,seller_raw=raw,seller_price=price,desc=discription,img=image)

        Seller.save()
        messages.success(request,'Successfully Made A Registration')



    return render(request,"seller.html")

