from django.db import models

# Create your models here.
class Product(models.Model):
    ITEM_CATEGORIES = [
        ('ACC', 'Accessories'),
        ('B', 'Bags'),
        ('C', 'Clothes'),
        ('EL', 'Electronics'),
        ('FD', 'Food'),
        ('FUR', 'Furniture + Home Deco'),
        ('K', 'Kitchen Apps'),
        ('NO', 'Not Food'),
        ('SH', 'Shoes'),
        ('SO', 'Socks'),
        ('N', 'New')
    ]
    product_name = models.CharField(max_length = 45)
    product_price = models.FloatField(default = 0)
    product_category = models.CharField(max_length=3, default='N', choices=ITEM_CATEGORIES)
    image = models.ImageField(upload_to= './images/', default = '')
    """
    not sure if these are needed
    """
    product_description = models.TextField(max_length= 10000)
    #product_status = models.BooleanField(max_length=5, blank = True) #in-queue, liked, in cart, purchased, or disliked
    def __str__(self):
        return self.product_name
