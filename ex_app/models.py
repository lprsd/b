from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BaseModel(models.Model):
    timestamp = models.DateTimeField()
    author = models.ForeignKey(User, blank=True, null=True)

    class Meta:
        abstract = True
        
class Ad(BaseModel):
    display_text = models.CharField(max_length=80)
    #title = models.CharField(max_length=80)
    
class PubSite(BaseModel):
    site_name = models.CharField(max_length=80)
    