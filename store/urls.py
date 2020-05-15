from django.urls import path
from . import views

urlpatterns = [
    path('store/', views.ProductsView, name='storehome'),
    path('product/<int:pk>/', views.ProductView, name='product'),
    path('new-product/', views.CreateProduct, name='form'),
    path('edit-product/<int:pk>/', views.EditProduct, name='edit'),
    path('delete-product/<int:pk>/', views.DeleteProduct, name='delete_product'),

]
