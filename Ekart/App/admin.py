from django.contrib import admin

# Register your models here.
from App.models import User,Customer,Product,Order,OrderItem,ShippingAddress,Category

admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Category)