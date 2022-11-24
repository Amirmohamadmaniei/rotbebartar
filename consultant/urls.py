from django.urls import path, re_path

from consultant import views

app_name = 'consultant'

urlpatterns = [
    path('all', views.ConsultantListView.as_view(), name='consultant_list'),
    path('search/', views.SearchConsultantView.as_view(), name='consultant_list_search'),
    path('filter', views.FilterConsultantView.as_view(), name='consultant_list_filter'),
    re_path(r'detail/(?P<slug>[-\w]+)/', views.ConsultantDetailView.as_view(), name='consultant_detail'),
    path('select/', views.SelectConsultantView.as_view(), name='consultant_select'),
]