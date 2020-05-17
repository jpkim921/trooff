import django_filters
from django_filters import CharFilter

from .models import *


class ProductFilter(django_filters.FilterSet):
        name = CharFilter(field_name="name", lookup_expr='icontains')

        class Meta:
            model = Product
            fields = '__all__'
            exclude = ['date', 'description', 'tags']
