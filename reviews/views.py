from .models import Review
from .forms import ReviewForm
from products.models import Product
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def reviews(request):

    reviews = Review.objects.all()
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            reviews = reviews.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'

    context = {
        'reviews': reviews,
        'current_sorting': current_sorting,
    }

    return render(request, 'reviews/reviews.html', context)


@login_required
def add_review(request, id):
    if not request.user:
        messages.error(request, 'Sorry, you need to log in do that.')
        return redirect(reverse('home'))

    reviews = Review.objects.all()
    product = Product.objects.get(id=id)
    form = ReviewForm(request.POST or None)

    if form.is_valid():
        rating = request.POST.get('rating')
        name = request.POST.get('name')
        title = request.POST.get('title')
        body = request.POST.get('body')
        review = Review(rating=rating, name=name, title=title, body=body, product=product)
        review.save()
        messages.info(request, 'You have successfully added a review!')
        return redirect(reverse('product_detail', args=[product.id]))

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
