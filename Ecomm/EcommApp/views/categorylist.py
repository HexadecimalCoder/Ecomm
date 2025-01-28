from EcommApp.models.category import Category
from django.shortcuts import render
from EcommApp.models.product import Product

def Category_List(request):
    print("Category_List view has been called.")  # Debug message
    categories = Category._get_all_categories()
    print("Categories from the database:", categories)


    
    products = Product.get_all_products()
    print("products:",products)


    return render(request, 'products.html', {'categories': categories,'products':products})