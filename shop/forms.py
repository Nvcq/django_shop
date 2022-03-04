from django.forms import ModelForm
from .models import Product

class productForm(ModelForm):
    use_required_attribute = False
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity']