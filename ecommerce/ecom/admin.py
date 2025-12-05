from django.contrib import admin
from ecom.models import product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=['id','name','price','specifications','img']
admin.site.register(product,ProductAdmin)
