from django.urls import path

from account import views

app_name = 'account'

urlpatterns = [
    path('login', views.LoginView.as_view(), name='login'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('profile/<int:pk>', views.UserProfileView.as_view(), name='profile'),
]
