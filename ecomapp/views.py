from django.shortcuts import render
from storeapp.models import Product,ReviewRating
# Create your views here.
def index(request):
    products=Product.objects.all().filter(is_available=True).order_by('-created_date')

    # Get the reviews
    for product in products:

     reviews = ReviewRating.objects.filter(product_id=product.id, status=True)


    context={
        "products":products,
        "reviews":reviews,
        }
    return render(request, 'index.html',context)