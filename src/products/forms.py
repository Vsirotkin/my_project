from django import forms
from django.forms import ModelForm
from .models import Product


class RowProductForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    price = forms.DecimalField()


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
        ]
