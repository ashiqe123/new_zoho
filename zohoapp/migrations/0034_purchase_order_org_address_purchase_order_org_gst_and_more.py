# Generated by Django 4.2.1 on 2023-07-06 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0033_rename_org_address_purchase_order_typ_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase_order',
            name='Org_address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='purchase_order',
            name='Org_gst',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='purchase_order',
            name='Org_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]