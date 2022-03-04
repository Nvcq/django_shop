from attr import fields
from django import forms
from django.forms import ModelForm
from .models import Product

class productForm(ModelForm):
    use_required_attribute = False
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity', 'image']


class quantityForm(forms.Form):
    newquantity = forms.IntegerField(label="Nombre d'article(s) ")