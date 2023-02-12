from .models import Review
from django import forms
from django.forms import ModelForm, TextInput, Textarea, NumberInput


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('rating', 'name', 'title', 'body')
        widgets = {
            'rating': NumberInput(attrs={
                'id': "output",
                'class': "text-light border-0",
                'style': 'width: 0%;',
                }),
            'name': TextInput(attrs={
                'class': "form-control border-dark rounded-0",
                'style': 'width: 100%;',
                }),
            'title': TextInput(attrs={
                'class': "form-control border-dark rounded-0",
                'style': 'width: 100%;',
                }),
            'body': Textarea(attrs={
                'class': "form-control border-dark rounded-0",
                'style': 'width: 100%;',
                'rows': 4
                }),
        }