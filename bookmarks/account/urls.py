from django.urls import include, path
from . import views

urlpatterns = [
    # previous login view
    # path('login/', views.user_login, name='login'),
    path('', include('django.contrib.auth.urls')),
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
]
