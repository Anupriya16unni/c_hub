import decimal
from django.shortcuts import render
import random
from datetime import date

from customer.models import Invoice
from shop.models import Item
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def  invoice(request):

    invoice_no=random.randint(1111,9999)
    
    current_date=today = date.today()
    
    if request.method=="POST":
        id = request.POST['p_name']
        phn=request.POST['phn']
        sname=request.POST["s_name"]
        qty=request.POST['v_qty']
        item_id = Item.objects.get(id = id)
        total_price = ( decimal.Decimal(float(qty)) * item_id.product_price)        

        invoice=Invoice(phone=phn,name=sname,invoice_number=invoice_no,date=current_date,  quantity=qty, item_id = item_id, total_price=total_price )
        invoice.save()

        obj = Item.objects.get(id = id)

        updatedQuantity = obj.available_qty - int(qty)

        products = Item.objects.filter(id = id).update(available_qty = updatedQuantity)


        if obj.available_qty < 20:
            products = Item.objects.filter(id = id).update(item_status = 'Less of stock')
        
        elif obj.available_qty <= 0 :
            products = Item.objects.filter(id = id).update(item_status = 'Out of stock')
        else:
            products = Item.objects.filter(id = id).update(item_status = 'In stock')

    product = Item.objects.all()

    total = Invoice.objects.all()

    grandTotal = 0

    for price in total:
        grandTotal = grandTotal + price.total_price

    return render (request,'invoice.html',{'product':product,'inv':invoice_no,'date':current_date, })


@csrf_exempt
def Fun_invo(request):
    invo_item=request.POST['item_name']
    print(invo_item)
    invoice_list=Item.objects.get(id=invo_item)
    return JsonResponse({'invo':invoice_list.product_price})