from django.contrib import admin
from .models import models, ShippingAddress, OrderItem, Order, Product, Customer

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)