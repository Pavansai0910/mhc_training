from django.db import models

class clothes(models.Model):
     product_id = models.CharField(primary_key=True, max_length=100)
     name= models.CharField(max_length=255)
     customer_id=models.CharField(unique=True,max_length=30)
     price = models.DecimalField(max_digits=10, decimal_places=2)

     def __str__(self):
          return f"{self.product_id} {self.name}"
