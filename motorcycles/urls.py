from django.contrib.auth.views import LogoutView
from django.urls import path

from motorcycles.views import Add

urlpatterns = [
    path('add/', Add.as_view(), name='Add'),
    # path('logout/', LogoutView.as_view(), name='logout'),
]
