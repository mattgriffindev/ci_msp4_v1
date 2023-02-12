from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about_us/', views.about_us, name='about_us'),
    path('contact/', views.contact, name='contact'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
    path('delivery/', views.delivery, name='delivery'),
    path('returns/', views.returns, name='returns'),
    path('payment/', views.payment, name='payment'),
]