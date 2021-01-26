from django.contrib import admin
from .models import *

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Shipping)
admin.site.register(Product)
# Register your models here

