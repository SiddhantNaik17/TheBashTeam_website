from django.contrib.auth.views import LogoutView
from django.urls import path
from django.views.generic import TemplateView

from accounts import views

urlpatterns = [
    path('orders/', TemplateView.as_view(template_name='accounts/orders.html'), name='orders'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.RegistrationView.as_view(), name='register'),
]
