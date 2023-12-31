from django.db import models
from datetime import datetime
from django.utils.text import slugify

# Create your models here.

class Product(models.Model):

    COLORS_CHOICES = [
        ('black', 'Black'),
        ('silver', 'Silver'),
        ('gold', 'Gold'),
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('purple', 'Purple'),
    ]

    name = models.CharField(max_length=255, verbose_name='Title')
    image = models.ImageField(upload_to='products/%y/%m/%d')
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    content = models.TextField()
    color = models.CharField(max_length=255, choices=COLORS_CHOICES)
    stock = models.IntegerField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    description = models.TextField()
    Additional_Information = models.TextField()
    Shipping_Returns = models.TextField()
    reviews = models.IntegerField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
    slug = models.SlugField(blank=True, null=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Title')
    slug = models.SlugField(max_length=255, unique=True)
    active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='categories/%y/%m/%d')

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=255, verbose_name='Title')
    slug = models.SlugField(max_length=255, unique=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
