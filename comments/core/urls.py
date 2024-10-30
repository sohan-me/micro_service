from django.urls import path, include
from . import views

urlpatterns = [
    path('comments/', views.CommentView.as_view()),
    path('posts/<int:pk>/comments/', views.PostCommentView.as_view())

]
