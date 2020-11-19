from django.urls import path

from products import views

urlpatterns = [
    path('add_product/', views.ProductAddView.as_view(), name='product-add'),
    path('<slug:slug>/', views.CategoryDetailView.as_view(), name='category-detail'),
    path('<slug:category>/<slug:slug>/', views.ProductDetailView.as_view(), name='product-detail'),
]
