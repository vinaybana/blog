from django.urls import path
from . import views
from . import urls


app_name = 'blog'

urlpatterns = [
    path('post/<str:slug>/edit/', views.post_edit, name='post_edit'),
    path('category/<str:slug>/edit/', views.category_edit, name='category_edit'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<str:slug>/', views.post_detail, name='post_detail'),
    path('category/<str:slug>/', views.category_detail, name='category_detail'),
    path('tag/<str:slug>/', views.tag_details, name='tag_details'),
    path('category/', views.category_list, name ='category_list'),
    path('tag/', views.tag_list, name ='tag_list'),
    path('', views.post_list, name ='post_list'),
    
]