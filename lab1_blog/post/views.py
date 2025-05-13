from django.shortcuts import render, get_object_or_404
from .models import Post, Author
from rest_framework import generics
from .serializers import AuthorSerializer, PostSerializer


def index(request):
    posts = Post.objects.all()
    return render(request, "index.html", {'posts': posts})

def post_details(request, post_id):
    # post = Post.objects.filter(id=post_id).first()
    post = Post.objects.get(id=post_id)
    return render(request, "details.html", {'post': post})

def author_profile(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    posts = author.posts.all()
    return render(request, "author_profile.html", {'author': author, 'posts': posts})

class AuthorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer