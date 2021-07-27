from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from App_posts.models import Posts
from django.contrib.auth.models import User
@login_required
def home(request):
    all_post = Posts.objects.all()
    if request.method=='GET':
        search = request.GET.get('search','')
        result = User.objects.filter(username__icontains=search)
    return render(request, 'App_posts/home.html', context={'all_post':all_post, 'search':search, 'result':result})
# Create your views here.