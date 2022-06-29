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



class ProductForm(forms.Form):
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
    email = forms.EmailField()
    price = forms.DecimalField(initial=200.00)


    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('ru'):
            raise forms.ValidationError('it is not a valid email address!')
        return email

'''
 class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
        ]
'''
