from django.shortcuts import render
from storeapp.models import Product
# Create your views here.
def index(request):
    product=Product.objects.all().filter(is_available=True)
    context={
        "product":product}
    return render(request, 'index.html',context)