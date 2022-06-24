from django.shortcuts import redirect, render
import random
from datetime import date
from customer.models import Invoice
from shop.models import Bill, Item
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def  item_master(request):
    if request.method=="POST":
        item_name=request.POST["i_name"]
        item_price=request.POST['i_price']
        available_quantity=request.POST['i_qty']
        code=request.POST["i_code"]
        status=request.POST["i_status"]

        stock=Item(item_name=item_name,product_price=item_price,available_qty=available_quantity,product_code=code,item_status=status)
        stock.save()
        request.session['product_id']=stock.id
    return render (request,'item_master.html')

def  bill(request):
    bill_no=random.randint(1111,9999)
    current_date=today = date.today()
    if request.method=="POST":
        sname=request.POST["s_name"]
        item_id = request.POST['item_name']

        i_name=request.POST['p_name']
        qty=request.POST['v_qty']
        price=request.POST['v_price']

        bill=Bill(supplier_name=sname,bill_number=bill_no,bill_date=current_date,item_name=i_name,quantity=qty,price=price, )
        bill.save()
    product=Item.objects.all()
    return render (request,'bill.html',{'product':product,'billno':bill_no,'date':current_date})



@csrf_exempt
def fun_check(request):
    item_id = request.POST['item_name']
    price_lst = Item.objects.get(id=item_id) 
    return JsonResponse({'pr_lst':price_lst.product_price})       

def  master(request):
    
    return render (request,'master.html')

def inventory(request):
    total=request.POST["total"]
