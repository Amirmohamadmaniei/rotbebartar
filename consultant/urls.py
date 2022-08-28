from django.urls import path

from consultant import views

app_name = 'consultant'

urlpatterns = [
    path('all', views.ConsultantListView.as_view(), name='consultant_list'),
    path('detail/<int:pk>', views.ConsultantDetailView.as_view(), name='consultant_detail'),
]
