from django.contrib import admin
from loot_backend.models import Product

# Register your models here.
admin.site.register(Product, admin.ModelAdmin)
