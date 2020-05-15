from django.urls import path
from . import views

urlpatterns = [
    path('store/', views.ProductsView, name='storehome'),
    path('product/<int:pk>/', views.ProductView, name='product'),
    path('new-product/', views.CreateProduct, name='form'),

]
