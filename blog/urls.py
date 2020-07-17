from django.urls import path
from . import views
from . import urls
# from taggit.models import Tag

app_name = 'blog'

urlpatterns = [
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
	path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('category/<str:slug>/edit/', views.category_edit, name='category_edit'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('category/<str:slug>/', views.category_detail, name='category_detail'),
    path('tag/<str:slug>/', views.tag_details, name='tag_details'),
    path('category/', views.category_list, name ='category_list'),
    path('tag/', views.tag_list, name ='tag_list'),
    path('', views.post_list, name ='post_list'),
    
]