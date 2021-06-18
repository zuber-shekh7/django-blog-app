from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.list_post, name='list-post'),
    path('<int:pk>/', views.detail_post, name='detail-post'),
    path('<int:pk>/edit/', views.update_post, name='update-post'),
    path('<int:pk>/delete/', views.delete_post, name='delete-post'),
    path('new/', views.create_post, name='create-post'),
]