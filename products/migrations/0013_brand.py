# Generated by Django 5.0 on 2023-12-19 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
