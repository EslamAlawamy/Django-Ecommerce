# Generated by Django 5.0 on 2023-12-17 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='date',
        ),
    ]