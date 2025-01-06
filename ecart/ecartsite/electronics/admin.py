from django.contrib import admin

from . models import electronics
@admin.register(electronics)
class electronicsAdmin(admin.ModelAdmin):
    list_display=('product','price','customer_id')
