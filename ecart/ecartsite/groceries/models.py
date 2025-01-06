from django.db import models

class grocey(models.Model):
    product_id = models.CharField(max_length=100),
    name = models.CharField(max_length=200),
    price = models.DecimalField(max_digits=10, decimal_places=2)
   