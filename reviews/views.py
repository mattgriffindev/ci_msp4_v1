from .models import Review
from .forms import ReviewForm
from products.models import Product
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages


def all_reviews(request):
    reviews = Review.objects.all()

    return render(request, 'reviews/reviews.html')


def add_review(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ReviewForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'reviews/add_review.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)
