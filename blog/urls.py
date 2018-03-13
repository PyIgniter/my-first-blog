from django.urls import path
# from django.conf.urls import url
from . import views
# from django.urls import include, re_path

urlpatterns = [
    # url(r'^$', views.post_list, name='post_list'),
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # re_path(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    # url(r'^post/new/$', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    # url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    
]