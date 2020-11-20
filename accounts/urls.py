from django.contrib.auth.views import LogoutView
from django.urls import path

from accounts import views

urlpatterns = [
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
