
from django.contrib import admin

# Register your models here.
from menu.models import Menu, Order, OrderedMenu


# admin.site.register(Menu)

admin.site.register(Menu),
admin.site.register(Order),
admin.site.register(OrderedMenu)
