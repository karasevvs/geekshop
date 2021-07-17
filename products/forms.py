from django import forms
from products.models import ProductCategory, Product
from django.contrib.auth.forms import UserChangeForm

class ProductCategoryForm(UserChangeForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))

    class Meta:
        model = ProductCategory
        fields = ('name', 'description')


class ProductForm(UserChangeForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    price = forms.DecimalField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    quantity = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    category = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))

    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'quantity', 'category')