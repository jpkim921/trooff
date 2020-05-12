from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.registerUser, name="register"),
    path('login/', views.login, name="login"),
    path('products/', views.products, name="products"),
    path('customer/<int:pk>/', views.customer, name="customer"),
    path('create_order/<str:pk>', views.createOrder, name="create_order"),
    path('update_order/<str:pk>', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>', views.deleteOrder, name="delete_order"),
]
