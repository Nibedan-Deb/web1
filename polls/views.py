from django.shortcuts import render
from polls.models import Shop
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return render(request, 'index.html',)

def about(request):
    return render(request, 'about.html',)

def blog(request):
    return render(request, 'blog.html',)

def shop(request):
    shop_Data = Shop.objects.all()
    return render(request, 'shop.html',context={'shop_data':shop_Data}) 

def contact(request):
    return render(request, 'contact.html',)

def cart(request):
    return render(request, 'cart.html',)

def products(request, id):
    product = get_object_or_404(Shop, id=id)
    return render(request, 'products.html', context={'product': product})