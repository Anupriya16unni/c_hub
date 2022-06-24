# Generated by Django 4.0.2 on 2022-06-24 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_remove_bill_item_name_remove_bill_price_bill_item_id'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='item_name',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='price',
        ),
        migrations.AddField(
            model_name='invoice',
            name='item_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='shop.item'),
            preserve_default=False,
        ),
    ]