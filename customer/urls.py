from django.urls import path
from .import views
app_name="invoice"

urlpatterns = [

    path('invoice', views.invoice, name="invoice"),
    path('invoice_list',views.Fun_invo,name="invoice_list"),
    
   



]