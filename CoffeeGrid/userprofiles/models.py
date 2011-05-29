from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User)
    blogurl = models.URLField()
    location = models.CharField(max_length=200)
    intro = models.CharField(max_length=500)
    thoughts = models.CharField(max_length=500)
    twitter = models.CharField(max_length=15)
    avatar = models.URLField()
    
    def __unicode__(self):
        return self.user.username + " (profile)"