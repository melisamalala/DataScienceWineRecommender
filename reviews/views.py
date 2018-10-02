from django.shortcuts import render, get_object_or_404
from .models import Review, Wine


# Create your views here.

def review_list(request):

    latest_review_list = Review.objects.order_by('-pub_date')
    context = {'latest_review_list': latest_review_list}

    return render (request,
                   'reviews/review_list.html',
                   context)

def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'reviews/review_detail.html', {'review': review})



def wine_list(request):
    wine_list = Wine.objects.order_by('-name')
    context = {'wine_list':wine_list}
    return render(request,
                  'reviews/wine_list.html',
                  context)

def wine_detail(request, wine_id):
    wine = get_object_or_404(Wine, pk=wine_id)
    return render (request,
                   'reviews/wine_detail.html',
                   {'wine':wine})