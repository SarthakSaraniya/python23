from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('rent-venue/',views.rent_venue,name='rent-venue'),
    path('shows-events/',views.shows_events,name='shows-events'),
    path('tickets/',views.tickets,name='tickets'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('change-password/',views.change_password,name='change-password'),
    path('forgot-password/',views.forgot_password,name='forgot-password'),
    path('verify-otp/',views.verify_otp,name='verify-otp'),
    path('new-password/',views.new_password,name='new-password'),
    path('profile/',views.profile,name='profile'),
    path('manager-add-event/',views.manager_add_event,name='manager-add-event'),
]