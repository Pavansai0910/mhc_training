from . import views
from django.urls import path
urlpatterns=[
    path('',views.clothes_list,name='clothes'),
    path('product',views.product_add,name='addclothe'),
   
]