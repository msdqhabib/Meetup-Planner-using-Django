from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:meetup_slug>/success/', views.confirmation_registration, name='confirmation-registration'),
    path('<slug:meetup_slug>/', views.meetup_details, name='meetup-details'),
]