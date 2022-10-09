from django.urls import path
from Buyer import views

urlpatterns = [
    
    path('',views.index),
]