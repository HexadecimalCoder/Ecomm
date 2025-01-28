from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from EcommApp.models.product import Product
from EcommApp.views.cart_utils import get_or_create_cart
from django.http import JsonResponse
from EcommApp.models.cart import CartItem

def Cart(request):
    if not request.session['user_id']:
        messages.error(request, "Please log in to view your cart.")
        return redirect('login')

    cart = get_or_create_cart(request.session['user_email'])
    cart_items = cart.items.all() 
    return render(request, "cart.html", {"cart_items": cart_items})


def add_to_cart(request, product_id):
    if not request.session.get('user_id'): 
        messages.error(request, "Please log in to add items to the cart.")
        return redirect('login')  

    product = get_object_or_404(Product, id=product_id)
    cart = get_or_create_cart(request.session.get('user_email'))  

    cart_item=CartItem.objects.filter(cart=cart,product=product).first()

    if cart_item:
        messages.error(request, f"{product.name} is already in your cart.")
    else:
        cart_item=CartItem(cart=cart,product=product,quantity=1)
        cart_item.save()
        messages.success(request, f"{product.name} has been added to your cart.")

    
   
    

    if 'from_product_detail' in request.GET:
        return redirect('product_detail', product_id=product.id)  
    return redirect('products')  


def cart_view(request):
    if request.session['user_id']:
        print("Login Successfully.")
        cart = get_or_create_cart(request.session['user_email'])
        return render(request, "cart.html", {"cart_items": cart.items.all()})
    else:
        print("Login Failed.")
        messages.error(request, "Please log in to view your cart.")
        return redirect('login')

   



def Remove_From_Cart(request,product_id):
    if not request.session.get('user_id'):
        messages.error(request, "Please log in to remove items from the cart.")
        return redirect('login')

    cart=get_or_create_cart(request.session.get('user_email'))

    if not cart:
        messages.error(request,"Cart not found.")
        return redirect("cart_view")
    
    cart_item=CartItem.objects.filter(cart=cart,product_id=product_id).first()

    if not cart_item:
        messages.error(request,"Item not found in your cart.")
    else:
        cart_item.delete()
        messages.success(request, "Item removed from the cart.")
        
        return redirect('cart_view')
    
    
        
        
def increment_quantity(request,product_id):
    if not request.session.get('user_id'):
        messages.error(request, "Please log in to update your cart.")
        return redirect('login')
    
    cart=get_or_create_cart(request.session.get('user_email'))
    cart_item=CartItem.objects.filter(cart=cart,product_id=product_id).first()


    if cart_item:
        cart_item.quantity +=1
        cart_item.save()
        messages.success(request,f"Updated quantity of {cart_item.product.name} to {cart_item.quantity}.")
    else:
        messages.error(request, "Item not found in your cart.")
        
    return redirect("cart_view")



def decrement_quantity(request,product_id):
    if not request.session.get('user_id'):
        messages.error(request, "Please log in to update your cart.")
        return redirect('login')
    
    cart=get_or_create_cart(request.session.get("user_email"))
    cart_item=CartItem.objects.filter(cart=cart,product_id=product_id).first()


    if cart_item:
        if cart_item.quantity >1:
            cart_item.quantity -=1
            cart_item.save()
            messages.success(request, f"Updated quantity of {cart_item.product.name} to {cart_item.quantity}.")
            
        else:
            cart_item.delete()
            messages.success(request, f"{cart_item.product.name} was removed from the cart.")
    else:
        messages.error(request, "Item not found in your cart.")
    
    return redirect("cart_view")

            

    
def Cart_Totle_Count(request):
    if not request.session.get('user_id'):
        return JsonResponse({"error": "Please log in to update your cart."}, status=403)

    cart = get_or_create_cart(request.session['user_email'])
    cart_items = cart.items.all()
    total_price = sum(item.product.discount * item.quantity for item in cart_items)

    return JsonResponse({"total_price": total_price}, status=200)