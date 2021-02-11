from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Product


# Create your views here.
def hello_world(request):
    return HttpResponse("Hello World")

class ProductList(ListView):
    model = Product
