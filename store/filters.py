import django_filters
from django_filters import CharFilter, NumberFilter

from .models import *


class ProductFilter(django_filters.FilterSet):
        name = CharFilter(field_name="name", lookup_expr='icontains')
        # price = django_filters.NumberFilter()
        price__gt = NumberFilter(field_name='price', lookup_expr='gt')
        price__lt = NumberFilter(field_name='price', lookup_expr='lt')
        
        class Meta:
            model = Product
            # fields = '__all__'
            fields = ['name', 'category']
            # exclude = ['date', 'description', 'tags']
