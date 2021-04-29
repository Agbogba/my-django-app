from django.contrib import admin
from .models import Post
from .models import Item, OrderItem, Order

admin.site.register(Post)
admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order)
