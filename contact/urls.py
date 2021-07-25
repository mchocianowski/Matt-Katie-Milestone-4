from django.contrib import admin
from django.urls import path
from contact import views as contact_views

urlpatterns = [
    path('', contact_views.contact_view, name='contact'),
    path('success/', contact_views.successView, name='success'),
]