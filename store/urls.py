from django.urls import path
from . import views

urlpatterns = [
    path('store/', views.ProductsView, name='store'),
    path('product/<int:pk>/', views.ProductView, name='product'),

]
