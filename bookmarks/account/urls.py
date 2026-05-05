from django.urls import path, include
from . import views

app_name = 'account'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
    path('', include('django.contrib.auth.urls')),
]
