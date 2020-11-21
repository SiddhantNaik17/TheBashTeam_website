from django.urls import path

from home import views

urlpatterns = [
    path('', views.HomepageView.as_view(), name='homepage'),
    path('bot-message/', views.bot_message, name='bot-message'),
]
