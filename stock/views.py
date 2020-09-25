
from django.shortcuts import render
from .models import Product 
# from django.http import HttpResponse

# Create your views here.
def index(request):
    product = Product.objects.all()
    return render(request, 'frontend/index.html',{'products':product})

def about(request):
    return render(request, 'frontend/about.html')

def contact(request):
    return render(request, 'frontend/contact.html')