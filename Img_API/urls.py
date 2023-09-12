from django.urls import path
from . import views
from django.urls import include





urlpatterns = [
    
   
    path('home', views.index, name='home'),
    path('create_img_type/', views.create_img_type, name='create_img_type'),
    path('add_img_withTypeType/', views.add_img_withTypeType, name='add_img_withTypeType'),
    path('add_imgs/', views.add_imgs, name='add_imgs'),
    

   
]