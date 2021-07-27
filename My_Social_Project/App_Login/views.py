from django.contrib.auth.models import User
from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
from App_Login.forms import CreateNewUser, EditProfile
from App_Login.models import UserProfile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from App_Login.models import Follow


from App_posts import forms
from App_posts.models import Posts
def sign_up(request):
    form = CreateNewUser()
    registered = False
    if request.method=='POST':
        form = CreateNewUser(data=request.POST)
        if form.is_valid():
            user = form.save()
            registered = True
            user_profile = UserProfile(user=user)
            user_profile.save()
            return HttpResponseRedirect(reverse('App_Login:login'))
    return render(request, 'App_Login/signup.html', context={'form':form})


def login_page(request):
    form = AuthenticationForm()
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user=authenticate(username=username, password = password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('App_posts:home'))
                

    return render(request,'App_login/login.html', context={'form':form})


@login_required
def edit_profile(request):
    current_user = UserProfile.objects.get(user=request.user)
    form = EditProfile(instance=current_user)
    if request.method=='POST':
        form = EditProfile(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            form.save()
            form = EditProfile(instance=current_user)
            return HttpResponseRedirect(reverse('App_Login:profile'))
    return render(request, 'App_login/profile.html', context={'form':form})


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_Login:login'))

@login_required
def profile(request):
    
    form = forms.PostForm()
    if request.method=='POST':
        form = forms.PostForm(request.POST, request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('home'))
    return render(request, 'App_Login/user.html', context={'form':form,})


@login_required
def user(request,username):
    other_user = User.objects.get(username=username)
    already_following = Follow.objects.filter(following = other_user, follower = request.user)
    if other_user==request.user:
        return HttpResponseRedirect(reverse('App_Login:profile'))
    return render(request, 'App_Login/other_user.html', context={'other_user':other_user, 'already_following':already_following})


@login_required
def follow(request, username):
    following_user = User.objects.get(username=username)
    follower_user = request.user
    already_following = Follow.objects.filter(following = following_user, follower = follower_user)
    if not already_following:
        followed_user = Follow(follower=follower_user,following=following_user)
        followed_user.save()

    return HttpResponseRedirect(reverse('App_Login:user',kwargs={'username':username}))


@login_required
def unfollow(request, username):

    unfollowing_user = User.objects.get(username=username)
    unfollower_user = request.user
    already_following = Follow.objects.filter(following = unfollowing_user, follower = unfollower_user)
    already_following.delete()

    return HttpResponseRedirect(reverse('App_Login:user', kwargs={'username':username}))

# Create your views here.
