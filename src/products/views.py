from django.shortcuts import render, get_object_or_404
from .models import Product


def product_detail_view(request):
    obj = get_object_or_404(Product, pk=1)
    '''
    context = {
        'title': obj.title,
        'description': obj.description,
    }
    '''
    context = {
        'object': obj,
    }

    return render(request, 'products/product_detail_view.html', context)
