from django.shortcuts import render, get_object_or_404
from .forms import *
from .models import Product


def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm

    context = {
        'form': form,
    }
    return render(request, 'products/product_create.html', context)

'''
def product_create_view(request):
    my_form = RowProductForm()

    if request.method == 'POST':
        my_form = RowProductForm(request.POST)
        if my_form.is_valid():
            Product.objects.create(**my_form.cleaned_data)

        my_form = RowProductForm

    context = {
        'form': my_form,
    }

    return render(request, 'products/product_create.html', context)

def product_detail_view(request):
    obj = get_object_or_404(Product, pk=1)

    context = {
        'object': obj,
    }

    return render(request, 'products/product_detail_view.html', context)
'''
