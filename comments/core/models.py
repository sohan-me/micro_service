from django.db import models

# Create your models here.

class Comment(models.Model):
    post_id = models.IntegerField()
    text = models.TextField(max_length=1000)
    
    def __str__(self):
        return str(self.post_id)
    
    
