from django.urls import path, include
from . import views

urlpatterns = [
    path('posts/', views.PostView.as_view()),

]
