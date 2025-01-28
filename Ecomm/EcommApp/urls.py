from django.urls import path
from .views.home import Home
from django.conf.urls.static import static
from django.conf import settings
from .views.signup import Sign_up
from .views.login import Login,logout
from .views.product import Product_View
from .views.productDetails import product_detail
from .views.categorylist import Category_List
from .views.cart_count import Cart_Count
from .views.forgetPassword import ForgetPassword
from .views.verifyOtp import VeryfyOTP
from .views.resetPassword import ResetPassword
from .views.userProfile import UserProfile
from .views.wishlist import Wishlist,add_to_wishlist,remove_from_wishlist
# from .views.whishlistCount import Wishlist_Count
from .views.cart import add_to_cart,Remove_From_Cart,increment_quantity,decrement_quantity,cart_view,Cart_Totle_Count
from .views.checkout_page import Chckout_Page,Checkout_View


urlpatterns = [
    path("",Home,name="home"),
    path("signup",Sign_up.as_view(),name="signup"),
    path("login",Login.as_view(),name="login"),
    path("logout",logout,name="logout"),
    path("products",Product_View,name="products"),
    path("productdetails/",product_detail,name="productdetails"),
    path("categorylist",Category_List,name="categorylist"),
    path("product/<int:product_id>/", product_detail, name="product_detail"),  
    path("cart/add/<int:product_id>/", add_to_cart, name="add_to_cart"),  
    path("cart/remove/<int:product_id>/", Remove_From_Cart, name="remove_from_cart"),  
    path("cart/increment/<int:product_id>/", increment_quantity, name="cart_increment"),  
    path("cart/decrement/<int:product_id>/", decrement_quantity, name="cart_decrement"),  
    path("home", Home, name="home"), 
    path("cart", cart_view, name="cart_view"), 
    path("cartcount/", Cart_Count, name="Cart_Count"), 
    path("cart/total/", Cart_Totle_Count, name="cart_total"), 
    path("checkout_page", Chckout_Page, name="checkout_page"), 
    path("checkout/process", Checkout_View, name="checkout_view"),
    path("forget-password",ForgetPassword.as_view(),name="forgetpassword"),
    path("verify-otp", VeryfyOTP.as_view(), name="verifyotp"), 
    path("wishlist",Wishlist,name='wishlist'),
    path("reset-password", ResetPassword.as_view(), name="resetpassword"),
    path("user-profile", UserProfile.as_view(), name="userprofile"), 
    path("wishlist",Wishlist,name='wishlist'),
    path("wishlist/add/<int:product_id>/",add_to_wishlist,name="add_to_wishlist"),
    path("wishlist/remove/<int:product_id>/",remove_from_wishlist,name="remove_from_wishlist"),

    # path("wishlistcount/", Wishlist_Count, name="Wishlist_Count"),



] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
