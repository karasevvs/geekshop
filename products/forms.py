from django import forms
from products.models import ProductCategory, Product
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

class ProductCategoryForm(UserChangeForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))

    class Meta:
        model = ProductCategory
        fields = ('name', 'description')
