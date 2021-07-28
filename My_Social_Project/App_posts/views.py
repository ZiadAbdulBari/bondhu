from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from App_posts.models import Like, Posts
from App_Login.models import Follow
from django.contrib.auth.models import User

@login_required
def home(request):
    # all_post = Posts.objects.all()
    following_user = Follow.objects.filter(follower=request.user)
    all_post = Posts.objects.filter(author__in=following_user.values_list('following'))
    already_liked = Like.objects.filter(user=request.user)
    if request.method=='GET':
        search = request.GET.get('search','')
        result = User.objects.filter(username__icontains=search)
    return render(request, 'App_posts/home.html', context={'all_post':all_post, 'search':search, 'result':result, 'already_liked':already_liked})

@login_required
def like(request,id):
    liked_post = Posts.objects.get(pk=id)
    liker = request.user
    already_liked = Like.objects.filter(post=liked_post,user=liker)

    if not already_liked:
        liked = Like(post=liked_post,user=liker)
        liked.save()
    print(already_liked)
    return HttpResponseRedirect(reverse('home'))

@login_required
def unlike(request, id):
    liker = request.user
    liked_post = Posts.objects.get(pk=id)
    already_liked = Like.objects.filter(post=liked_post,user=liker)
    already_liked.delete()
    return HttpResponseRedirect(reverse('home'))
    
# Create your views here.