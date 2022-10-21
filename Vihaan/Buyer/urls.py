from django.urls import path
from Buyer import views

urlpatterns = [
    
    path('',views.index),
    path('signin',views.signin),
    path('signup',views.signup),
    path('logout',views.logout),
]