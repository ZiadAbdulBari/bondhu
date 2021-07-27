from django.urls import path
from django.urls.resolvers import URLPattern
from App_posts import views


app_name = 'App_posts'

urlpatterns=[
    path('', views.home, name='home')
]