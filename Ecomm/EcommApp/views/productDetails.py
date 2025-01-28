from EcommApp.models.product import Product
from django.shortcuts import render,get_object_or_404


def product_detail(request, product_id):
    product=get_object_or_404(Product,id=product_id)
    return render(request,'productDetails.html',{'product':product})