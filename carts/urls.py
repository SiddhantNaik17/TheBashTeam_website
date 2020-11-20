from django.urls import path

from carts import views

urlpatterns = [
    path('', views.CartDetailView.as_view(), name='cart-detail'),
    path('add_product/', views.cart_add_product, name='cart-add-product'),
    path('checkout/', views.CheckoutView.as_view(), name='cart-checkout'),
    path('remove_product/', views.cart_remove_product, name='cart-remove-product'),
]
