from django.urls import path
from . import views

urlpatterns = [
    path('review/<int:id>', views.add_review, name='add_review'),
]
