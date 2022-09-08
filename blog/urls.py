from django.urls import path, re_path

from blog import views

app_name = 'blog'

urlpatterns = [
    path('all', views.BlogListView.as_view(), name='blog_list'),
    re_path(r'detail/(?P<slug>[-\w]+)/', views.BlogDetail.as_view(), name='blog_detail'),
    re_path(r'unlike/(?P<slug>[-\w]+)/', views.unlike, name='blog_unlike'),
    re_path(r'like/(?P<slug>[-\w]+)/', views.LikeView.as_view(), name='blog_like'),
]