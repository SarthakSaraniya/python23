from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('speaker/',views.speaker,name='speaker'),
    path('schedule/',views.schedule,name='schedule'),
    path('blog/',views.blog,name='blog'),
    path('contact/',views.contact,name='contact'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('change-password/',views.change_password,name='change-password'),
    path('forgot-password/',views.forgot_password,name='forgot-password'),
    path('verify-otp/',views.verify_otp,name='verify-otp'),
    path('new-password/',views.new_password,name='new-password'),
    path('profile/',views.profile,name='profile'),
    path('manager-add-event/',views.manager_add_event,name='manager-add-event'),
    path('manager-view-event/',views.manager_view_event,name='manager-view-event'),
    path('manager-edit-event/<int:pk>/',views.manager_edit_event,name='manager-edit-event'),
    path('manager-delete-event/<int:pk>/',views.manager_delete_event,name='manager-delete-event'),
]