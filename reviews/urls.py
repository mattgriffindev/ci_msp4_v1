from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_reviews, name='reviews'),
    path('<int:product_id>/', views.add_review, name='add_review'),
]
