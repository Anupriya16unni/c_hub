from django.urls import path
from .import views

urlpatterns = [

    path('', views.item_master, name="item_master"),
    path('bill', views.bill, name="bill"),
    path('price_list',views.fun_check,name='price_list'),

]