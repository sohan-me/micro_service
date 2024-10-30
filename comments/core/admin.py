from django.contrib import admin
from .models import Comment
# Register your models here.

@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    list_display = ['post_id', 'text']
    
    