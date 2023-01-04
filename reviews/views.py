from .models import Review
from .forms import ReviewForm
from products.models import Product
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages


def all_reviews(request):
    reviews = Review.objects.all()

    template = 'reviews/reviews.html'
    context = {
        'reviews': reviews,
    }
    return render(request, template, context)


def add_review(request, id):
    reviews = Review.objects.all()
    product = Product.objects.get(id=id)
    form = ReviewForm(request.POST or None)

    if form.is_valid():
        name = request.POST.get('name')
        title = request.POST.get('title')
        body = request.POST.get('body')
        review = Review(name=name, title=title, body=body, product=product)
        review.save()
        messages.success(request, 'Successfully added a review!')

    template = 'reviews/add_review.html'
    form = ReviewForm()
    context = {
        'form': form,
        'reviews': reviews,
        'product': product,
    }
    return render(request, template, context)
