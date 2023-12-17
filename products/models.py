from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='photos/%y/%m/%d')
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    content = models.TextField()
    color = models.CharField(max_length=255)
    stock = models.IntegerField()
    category = models.CharField(max_length=255)
    description = models.TextField()
    Additional_Information = models.TextField()
    Shipping_Returns = models.TextField()
    reviews = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
