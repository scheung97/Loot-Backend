from django.urls import path
from django.contrib import admin
from .views import hello_world, ProductList

urlpatterns=[
    path('admin/', admin.site.urls),
    path('', hello_world),
    path('products/', ProductList.as_view(), name = 'products'),
]
