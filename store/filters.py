import django_filters
from django_filters import CharFilter, NumberFilter, MultipleChoiceFilter
from django import forms

from .models import *

class ProductFilter(django_filters.FilterSet):

    name = CharFilter(field_name="name",
                      lookup_expr='icontains', label="Product Name", widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    category = MultipleChoiceFilter(choices=Product.CATEGORY, field_name='category', label="Category",
                            widget=forms.SelectMultiple(attrs={'class': 'form-control form-control-sm'}))
    price__gt = NumberFilter(field_name='price',
                             lookup_expr='gt', label="Minimum Price", widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm'}))
    price__lt = NumberFilter(field_name='price',
                             lookup_expr='lt', label="Maximum Price", widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm'}))

    class Meta:
        model = Product
        # fields = '__all__'
        fields = ['name', 'category']
        # exclude = ['date', 'description', 'tags']
