from django.db import models

# Create your models here.
class Product(models.Model): 
    product_name = models.CharField(max_length = 45)
    product_price = models.IntegerField(default = 0)

    """
    not sure if these are needed
    """
    product_description = models.CharField(max_length= 10000)
    product_status = models.BooleanField(max_length=5)
    def __str__(self): 
        return self.product_name
