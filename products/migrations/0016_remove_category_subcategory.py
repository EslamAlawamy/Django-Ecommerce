# Generated by Django 5.0 on 2023-12-19 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_category_image_category_subcategory_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='subcategory',
        ),
    ]
