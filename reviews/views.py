from .models import Review
from .forms import ReviewForm
from products.models import Product
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def reviews(request):

    reviews = Review.objects.all()

    context = {
        'reviews': reviews,
    }

    return render(request, 'reviews/reviews.html', context)


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


@login_required
def delete_review(request, review_id):
    """ Delete a review from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    review = get_object_or_404(Review, pk=review_id)
    review.delete()
    messages.info(request, 'Review deleted!')
    return redirect(reverse('products'))
