from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
    path('about/', views.about, name='about'),
    path('team/', views.team, name='team'),
    path('projects/', views.projects, name='projects'),
    path('services/', views.services, name='services'),
    path('pricing/', views.pricing, name='pricing'),
    path('contact/', views.contact, name='contact'),
    path('sendnewsletter/', views.send_newsletter, name='send_newsletter'),
    path('booking/', views.booking, name='booking'),
]
