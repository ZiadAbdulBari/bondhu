from django.urls import path
from django.urls.resolvers import URLPattern
from App_posts import views


app_name = 'App_posts'

urlpatterns=[
    path('', views.home, name='home'),
    path('like/<int:id>', views.like, name='like'),
    path('unlike/<int:id>', views.unlike, name='unlike'),
]