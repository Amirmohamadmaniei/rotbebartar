from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('about-us', views.AboutUsView.as_view(), name='about_us'),
    path('contact-us', views.ContactUsView.as_view(), name='contact_us'),
    path('faq', views.FaqView.as_view(), name='faq'),
    path('', views.HomeView.as_view(), name='home'),
]
