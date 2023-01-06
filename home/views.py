from django.shortcuts import render, get_object_or_404
from products.models import Product

# Create your views here.


def index(request):
    """ return index page """

    products = Product.objects.all().order_by('id')[:4]

    context = {
        'products': products,
    }
    return render(request, 'home/index.html', context)
