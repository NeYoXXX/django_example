from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    # post views
    # path('', views.post_list, name='post_list'), # 基于函数
    path('',views.PostListView.as_view(),name='post_list'),  # 基于类
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
]