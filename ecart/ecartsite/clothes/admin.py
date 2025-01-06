from django.contrib import admin
from . models import clothes
@admin.register(clothes)
class clothesAdmin(admin.ModelAdmin):
    list_display=('product_id','name','customer_id','price')
