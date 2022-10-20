from django.shortcuts import render
from store.models import Product
# Create your views here.
def home(request):
    products=Product.objects.filter(is_available=True).order_by('-upload_date')
    context={
        'products':products,
    }
    
    return render(request,'home.html',context)