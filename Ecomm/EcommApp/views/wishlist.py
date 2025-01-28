from django.shortcuts import render,redirect
from django.contrib import messages
from EcommApp.views.whishlist_utility import get_or_create_wishlist
from django.shortcuts import get_object_or_404
from EcommApp.models.wishlist import WishlistItem
from EcommApp.models.product import Product


def Wishlist(request):
    if not request.session['user_id']:
        messages.error(request, "Please log in to view your cart.")
        return redirect('login')
    
    
    wishlist = get_or_create_wishlist(request.session['user_email'])
    wishlist_items = wishlist.items.all()

    return render(request,"wishlist.html",{"wishlist_items": wishlist_items})



def add_to_wishlist(request, product_id):
    if not request.session.get('user_id'):
        messages.error(request, "Please log in to add items to your wishlist.")
        return redirect('login')

    product = get_object_or_404(Product, id=product_id)
    wishlist = get_or_create_wishlist(request.session['user_email'])

    wishlist_item = WishlistItem.objects.filter(wishlist=wishlist, product=product).first()
    if wishlist_item:
        messages.error(request, f"{product.name} is already in your wishlist.")
    else:
        WishlistItem.objects.create(wishlist=wishlist, product=product)
        messages.success(request, f"{product.name} has been added to your wishlist.")
    return redirect('store')


def remove_from_wishlist(request, product_id):
    if not request.session.get('user_id'):
        messages.error(request, "Please log in to remove items from your wishlist.")
        return redirect('login')

    wishlist = get_or_create_wishlist(request.session['user_email'])
    wishlist_item = WishlistItem.objects.filter(wishlist=wishlist, product_id=product_id).first()

    if wishlist_item:
        wishlist_item.delete()
        messages.success(request, "Item removed from your wishlist.")
    else:
        messages.error(request, "Item not found in your wishlist.")
    return redirect('wishlist')