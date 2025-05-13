from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.index, name='index'),
    path('post/<int:post_id>/', views.post_details, name='post_details'),
    path('author/<int:author_id>/', views.author_profile, name='author_profile'),

    # DRF API endpoints
    path('authors/', views.AuthorListCreateAPIView.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', views.AuthorRetrieveUpdateDestroyAPIView.as_view(), name='author-detail'),
    path('posts/', views.PostListCreateAPIView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', views.PostRetrieveUpdateDestroyAPIView.as_view(), name='post-detail'),
]
