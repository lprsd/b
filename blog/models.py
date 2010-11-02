from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BaseBlogModel(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField()
    author = models.ForeignKey(User)

    class Meta:
        abstract = True
        
class Post(BaseBlogModel):
    title = models.CharField(max_length=80)
    
class Comment(BaseBlogModel):
    post = models.ForeignKey(Post)
    