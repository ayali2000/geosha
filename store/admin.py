from django.contrib import admin
from . models import *

# Register your models here.
class AdminProduct(admin.ModelAdmin):
    list_display = ["productname","price","description","image","date_added"]

class AdminOrder(admin.ModelAdmin):
    list_display = ["customer_name","phone_number","quantity","Address","date_ordered"]


admin.site.register(Product,AdminProduct)
admin.site.register(Order,AdminOrder)