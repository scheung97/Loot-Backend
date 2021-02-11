from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import hello_world, ProductList

urlpatterns=[
    path('admin/', admin.site.urls),
    path('', hello_world),
    path('products/', ProductList.as_view(), name = 'products'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
