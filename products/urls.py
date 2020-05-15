from django.urls import path
from . import views

urlpatterns = [
    path('store/', views.ProductsView, name='store'),
    
]
# urlpatterns = [
#     path('api/products/', views.ProductsApi),
#     path('api/products/<int:pk>/', views.ProductPage),
# ]
