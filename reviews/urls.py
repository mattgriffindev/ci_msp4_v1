from django.urls import path
from . import views

urlpatterns = [
    path('', views.reviews, name='reviews'),
    path('review/<int:id>', views.add_review, name='add_review'),
    path('delete/<int:review_id>/', views.delete_review, name='delete_review'),
]