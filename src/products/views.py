from django.shortcuts import render, get_object_or_404
from .forms import ProductForm
# from .models import Product

def product_create_view(request):
    context = {}

    return render(request, 'products/product_create.html', context)

'''
def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm

    context = {
        'form': form,
    }
    return render(request, 'products/product_create.html', context)


def product_detail_view(request):
    obj = get_object_or_404(Product, pk=1)

    context = {
        'object': obj,
    }

    return render(request, 'products/product_detail_view.html', context)
'''
