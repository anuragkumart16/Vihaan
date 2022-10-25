from django.shortcuts import render,Http404,redirect
from Buyer.models import Buyer_table
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request,"buyer.html")
def signin(request):
    if request.method== "POST":
        user_name=request.POST.get('user_name')
        passw=request.POST.get('password')
        user = authenticate(username=user_name, password=passw)

        if user is not None :
            login(request, user)
            return render(request, 'landbuyer.html')
        else:
            messages.error(request, 'Inavalid Credentials ,Please Try Again')
            return render(request, 'Buyer.html')
        
def signup(request):
    if request.method=="POST":
        # get the post parameters
        name=request.POST.get('buyer_name')
        phone=request.POST.get('buyer_phone')
        adhaar=request.POST.get('buyer_adhaar')
        password=request.POST.get('buyer_pass1')

        # Buyer=Buyer_table(buyer_name=name,buyer_phone=phone,buyer_adhaar=adhaar,buyer_pass1=password)
        # Buyer.save()

        #create the user
        myuser=User.objects.create_user(name,phone,password)
        myuser.save()

        messages.success(request,'Successfully Signed Up. You may Sign in now')
        return render(request, 'buyer.html')
    else:
        return Http404('not allowed')

def logout(request):
    return render(request,'buyer.html')

def land(request):
   # if request.method=='POST':
        return render(request, 'landbuyer.html')
    #else:
     #   raise Http404('Unaurthorised Access')
    