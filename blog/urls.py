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

    path('drafts/', views.post_draft_list, name='post_draft_list'),
    # url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    # url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),

    path('post/<int:pk>/remove/', views.post_remove, name='post_remove'),
    # url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),

    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    # url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),

    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
	path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    # url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
	# url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),

    
]