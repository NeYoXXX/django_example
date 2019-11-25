from django.urls import path,include
from rest_framework import routers

from . import views
from .feeds import LastestPostFeed

router = routers.SimpleRouter()
router.register(r'palce', views.Placeview, basename='palce')


app_name = 'blog'
urlpatterns = [
    # post views
    path('', views.post_list, name='post_list'), # 基于函数
    # path('',views.PostListView.as_view(),name='post_list'),  # 基于类
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('feed/', LastestPostFeed(), name='post_feed'),
    path('search/', views.post_search, name='post_search'),

    path(r'api/', include(router.urls)),
]