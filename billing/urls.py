from django.urls import path

from billing import views

urlpatterns = [
    path('initiate/', views.initiate, name='initiate-billing'),
    path('processing/', views.processing, name='processing'),
]
