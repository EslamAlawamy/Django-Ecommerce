from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.products, name='products'),
    path('<str:slug>', views.product, name='product'),
]
