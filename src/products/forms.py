from django import forms
from django.forms import ModelForm
from .models import Product

'''
class RowProductForm(forms.Form):
    title = forms.CharField(label='my title', widget=forms.TextInput(attrs={'placeholder': 'my name for input'}))
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'my description',
                'class': 'my_new_class',
                'rows': 5,
                'cols': 25,
            }
        )
    )
    price = forms.DecimalField(initial=200.00)
'''



class ProductForm(ModelForm):
    title = forms.CharField(
        label='my title',
        widget=forms.TextInput(
            attrs={'placeholder': 'my name for input'}
        )
    )
    description = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'my description',
                'class': 'my_new_class',
                'rows': 5,
                'cols': 25,
            }
        )
    )
    price = forms.DecimalField(initial=200.00)

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
        ]


    def clean_description(self):
        description = self.cleaned_data.get('description')
        if not 'VIK' in description:
            raise forms.ValidationError('it is not a valid value for description')
        return description
