from django.urls import path

from orders import views

urlpatterns = [
    path('confirmed/', views.order_confirmed, name='order-confirmed')
]
