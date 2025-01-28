from EcommApp.models.category import Category
from django.shortcuts import render
from EcommApp.models.product import Product

def Product_View(request):
    print("Category_List view has been called.")  # Debug message
    categories = Category._get_all_categories()
    print("Categories from the database:", categories)


    
    products = Product.get_all_products()
    print("products:",products)
    category_id=request.GET.get('category')

    if category_id :
        products=Product.get_all_products_by_categories_id(category_id)
    else:
        products = Product.get_all_products()


    return render(request, 'products.html', {'categories': categories,'products':products})