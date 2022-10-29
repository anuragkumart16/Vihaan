from django.urls import path
from Buyer import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('',views.index),
    path('signin',views.signin),
    path('signup',views.signup),
    path('logout',views.logout),
    #path('landbuyer',views.land),
    path('landbuyer',views.product_data)
]

#if settings.DEBUG :
   # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    