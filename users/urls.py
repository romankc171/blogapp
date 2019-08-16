from django.urls import path, include
from .views import (
		register,
		profile,
		
)


from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='entrance/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='entrance/logout.html'), name='logout'),
    path('', profile, name='profile'),
]


