from django import forms
from django.forms import fields
from App_posts.models import Posts,Like

class PostForm(forms.ModelForm):
    class Meta:
        model=Posts
        fields=('image','caption')