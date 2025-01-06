from django.db import models

class electronics(models.Model):
    product=models.CharField(max_length=20)
    price=models.CharField(max_length=30)
    customer_id=models.CharField(unique=True,primary_key=True,max_length=20)
    def __self__():
        return f"(self.product)(self.price)"
