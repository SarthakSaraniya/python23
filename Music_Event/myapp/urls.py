from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('track/',views.track,name='track'),
    path('blog/',views.blog,name='blog'),
    path('single-blog/',views.single_blog,name='single-blog'),
    path('elements/',views.elements,name='elements'),
    path('contact/',views.contact,name='contact'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
]