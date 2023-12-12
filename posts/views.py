from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer,UserSerializer
#from rest_framework import generics
from rest_framework import viewsets
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAdminUser



# class PostList(generics.ListCreateAPIView):
#     permission_classes=(IsAuthorOrReadOnly,)
#     queryset=Post.objects.all()
#     serializer_class=PostSerializer


# the viewsets and ModelVIewsets provides list and detail view
class PostViewSet(viewsets.ModelViewSet):
    permission_classes=(IsAuthorOrReadOnly,)
    queryset=Post.objects.all()
    serializer_class=PostSerializer



class UserViewSet(viewsets.ModelViewSet):
    serializer_class=UserSerializer
    queryset=get_user_model().objects.all()
    permission_classes=[IsAdminUser]
    



# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes=(IsAuthorOrReadOnly,)
#     queryset=Post.objects.all()
#     serializer_class=PostSerializer


# class UserList(generics.ListCreateAPIView):
#     queryset=get_user_model().objects.all()
#     serializer_class=UserSerializer


# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset=get_user_model().objects.all()
#     serializer_class=UserSerializer
