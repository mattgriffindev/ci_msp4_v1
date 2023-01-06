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


def about_us(request):
    """ A view that renders the about us page """

    return render(request, 'home/about_us.html')


def contact(request):
    """ A view that renders the contact us page """

    return render(request, 'home/contact.html')


def terms(request):
    """ A view that renders the terms and conditions page """

    return render(request, 'home/terms.html')


def privacy(request):
    """ A view that renders the privacy page """

    return render(request, 'home/privacy.html')
