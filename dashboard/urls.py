from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.DashBoardHomeView.as_view(), name='home'),
    path('statistics', views.DashBoardStatisticsView.as_view(), name='statistics')
]