# Generated by Django 5.0 on 2023-12-17 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('phone', 'Phone'), ('laptop', 'Laptop'), ('watch', 'Watch'), ('headphone', 'Headphone'), ('camera', 'Camera'), ('accessories', 'Accessories')], max_length=255),
        ),
    ]
