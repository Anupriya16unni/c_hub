from itertools import product
from django.db import models


# Create your models here.

class Item(models.Model):
    item_name=models.CharField(max_length=100)
    product_code=models.CharField(max_length=100)
    product_price=models.DecimalField(max_digits=5,decimal_places=2)
    available_qty=models.BigIntegerField()
    item_status=models.CharField(max_length=100)
    
    class Meta:
        db_table="item_master"

class Bill(models.Model):
    item_id=models.ForeignKey(Item,on_delete=models.CASCADE)
    supplier_name=models.CharField(max_length=100)
    bill_date=models.CharField(max_length=100)
    bill_number=models.IntegerField(null=True)
    quantity=models.BigIntegerField()
    
    class Meta:
        db_table="bill"







