from django.shortcuts import render,redirect
from EcommApp.models.checkout import ShippingAddress,Order,OrderItem,Payment
from EcommApp.models.product import Product
from django.contrib import messages
from EcommApp.views.cart_utils import get_or_create_cart
from EcommApp.models.user import User
from EcommApp.models.cart import CartItem,Cart


def Chckout_Page(request):
    if not request.session['user_id']:
        messages.error(request, "Please log in to view your cart.")
        return redirect('login')

    cart = get_or_create_cart(request.session['user_email'])
    cart_items = cart.items.all() 
    return render(request,"checkoutPage.html",{"cart_items": cart_items})


def Checkout_View(request):
    if request.method == 'POST':
        try:
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            email = request.POST.get('email')
            address1 = request.POST.get('address1')
            address2 = request.POST.get('address2')
            city = request.POST.get('city')
            state = request.POST.get('state')
            country = request.POST.get('country')
            zip_code = request.POST.get('zip_code')
            payment_method = request.POST.get('payment_method')

            u_id = int(request.session['user_id'])
            user = User.objects.get(id=u_id)
            cart = Cart.objects.get(user=user)
            cart_items = CartItem.objects.filter(cart=cart)  

           
            total_amount = sum(item.product.price * item.quantity for item in cart_items)

            shipping_address = ShippingAddress.objects.create(
                user=user,
                fname=fname,
                lname=lname,
                email=email,
                address1=address1,
                address2=address2,
                city=city,
                state=state,
                country=country,
                zip_code=zip_code,
            )
            shipping_address.save()

            
            order = Order.objects.create(
                user=user,
                shipping_address=shipping_address,
                total_amount=total_amount,
                status='pending'
            )
            order.save()

          
            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,  
                    quantity=item.quantity,
                    price=item.product.price 
                )

           
            payment = Payment.objects.create(
                order=order,
                payment_method=payment_method,
                payment_status='pending',
                amount_paid=total_amount
            )
            payment.save()

            
            cart.items.all().delete()


            print("Order Placed Successfully...")

            messages.success(request, "Order placed successfully!")
            return redirect("home")
        except Exception as e:
            print(f"Error: {str(e)}")
            print("Order placed failled.........")
            messages.error(request, f"Something went wrong: {str(e)}")
            return redirect('cart_view')
    return render(request, 'checkoutPage.html')
