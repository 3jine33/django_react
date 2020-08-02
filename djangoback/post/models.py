from django.db import models

# Create your models here.

class Post(models.Model) : 
    title = models.CharField(max_length=500) #제목
    content = models.TextField() # 본문
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)