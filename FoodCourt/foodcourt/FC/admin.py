from django.contrib import admin
from .models import MenuItem, Order, OrderItem, DayMenu,PunjabiItems

admin.site.register(MenuItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(DayMenu)
admin.site.register(PunjabiItems)

