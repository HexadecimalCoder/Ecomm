from django.contrib import admin
# from models.user import User
from EcommApp.models.user import User
# Register your models here.
admin.site.register(User) 

from EcommApp.models.category import Category
admin.site.register(Category)

from EcommApp.models.product import Product
admin.site.register(Product)


from EcommApp.models.cart import Cart
admin.site.register(Cart)

from EcommApp.models.checkout import Chckout,Order,OrderItem,Payment,ShippingAddress
admin.site.register(Chckout)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Payment)
admin.site.register(ShippingAddress)


from EcommApp.models.wishlist import  Wishlist,WishlistItem
admin.site.register(Wishlist)
admin.site.register(WishlistItem)
