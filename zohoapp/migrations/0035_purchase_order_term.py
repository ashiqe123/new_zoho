# Generated by Django 4.2.1 on 2023-07-08 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0034_purchase_order_org_address_purchase_order_org_gst_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase_order',
            name='term',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]