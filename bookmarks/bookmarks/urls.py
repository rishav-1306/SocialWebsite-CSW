from django.contrib import admin
from django.urls import include, path

from account import views

urlpatterns = [
	path('', views.user_login, name='home'),
	path('admin/', admin.site.urls),
	path('account/', include('account.urls')),
]