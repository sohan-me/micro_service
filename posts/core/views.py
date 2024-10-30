from django.shortcuts import render
from .serializers import PostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from rest_framework import status
import requests
# Create your views here.

class PostView(APIView):
    serializer_class = PostSerializer
    
    def get_queryset(self):
        return Post.objects.all()

    
    def get(self, request):
        queryset = self.get_queryset()
        formatted_posts = [self.formatpost(post) for post in queryset]
        return Response(formatted_posts, status=status.HTTP_200_OK)
    
    
    def formatpost(self, post):
        
        comments = requests.get(f'http://comments-backend:8001/api/posts/{post.id}/comments/')
        
        if comments.status_code == 200:
            comments = comments.json()
        else:
            comments = []
        
        return {
            'id':post.id,
            'title':post.title,
            'body':post.body,
            'comments':comments,
        }
        
    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)            


