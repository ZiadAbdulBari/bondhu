from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import DateTimeField

class Posts(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(upload_to='post_images', blank=True)
    caption = models.CharField(max_length=155, blank=True)
    upload_data = models.DateTimeField(auto_now_add=True, blank=True )
    update_data = models.DateTimeField(auto_now=True, blank=True)

class Like(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='likeed_post')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liker')
    date_created = models.DateTimeField(auto_now_add=True)
# Create your models here.
