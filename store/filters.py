import django_filters
from django_filters import CharFilter, NumberFilter
from django import forms

from .models import *


class ProductFilter(django_filters.FilterSet):
    name = CharFilter(field_name="name",
                      lookup_expr='icontains', label="Product Name", widget=forms.TextInput(attrs={'class': 'form-control'}))
                      
    price__gt = NumberFilter(field_name='price',
                             lookup_expr='gt', label="Minimum Price", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    price__lt = NumberFilter(field_name='price',
                             lookup_expr='lt', label="Maximum Price", widget=forms.NumberInput(attrs={'class': 'form-control'})

    class Meta:
        model = Product
        # fields = '__all__'
        fields = ['name', 'category']
        # exclude = ['date', 'description', 'tags']
