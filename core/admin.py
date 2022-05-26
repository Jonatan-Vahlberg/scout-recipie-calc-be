from django.contrib import admin

from core.models import Cart, CartItem, PortionGroup

# Register your models here.
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(PortionGroup)