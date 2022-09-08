from django.urls import path

from account import views

app_name = 'account'

urlpatterns = [
    path('login', views.LoginView.as_view(), name='login'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('profile', views.UserProfileView.as_view(), name='profile'),
    path('profile/edit/', views.UserEditProfileView.as_view(), name='profile_edit'),
    path('profile/add-blog/', views.AddBlogView.as_view(), name='profile_add_blog'),
]
