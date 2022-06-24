from tkinter import CASCADE
from django.db import models

from shop.models import Item

# Create your models here.

class Invoice(models.Model):
    item_id=models.ForeignKey(Item,on_delete=models.CASCADE)
    phone=models.BigIntegerField()
    name=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    invoice_number=models.IntegerField(null=True)
    quantity=models.BigIntegerField()
    total_price = models.DecimalField(max_digits=5,decimal_places=2)

    
    class Meta:
        db_table="invoice"