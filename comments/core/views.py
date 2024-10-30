from django.shortcuts import render
from .serializers import CommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Comment
from rest_framework import status
# Create your views here.

class CommentView(APIView):
    serializer_class = CommentSerializer
    
    def get_query_set(self):
        return Comment.objects.all()
    
    def get(self, request):
        queryset = self.get_query_set()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)



class PostCommentView(APIView):
    serializer_class = CommentSerializer
    
    def get_queryset(self, post_id):
        return Comment.objects.filter(post_id=post_id)
    
    def get(self, request, pk=None):
        try:
            post_id = pk
        except ValueError:
            return Response({"error": "Invalid post ID"}, status=status.HTTP_400_BAD_REQUEST)
        
        queryset = self.get_queryset(post_id)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    