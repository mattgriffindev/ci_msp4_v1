from .models import Review
from .forms import ReviewForm
from products.models import Product
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages


def all_reviews(request):
    reviews = Review.objects.all()

    context = {
        'reviews': reviews,
    }
    return render(request, 'reviews/reviews.html', context)


def add_review(request, id):
    post = Product.objects.get(id=id)
    form = ReviewForm(request.POST or None)
    if form.is_valid():
        name = request.POST.get('name')
        title = request.POST.get('title')
        body = request.POST.get('body')
        review = Review(name=name, title=title, body=body, product=post)
        review.save()
        messages.success(request, 'Successfully added a review!')
    else:
        messages.error(request, 'Failed to add review. Please ensure the form is valid.')

    template = 'reviews/add_review.html'
    form = ReviewForm()
    context = {
        "form": form
    }
    return render(request, template, context)
