from .models import Review
from django import forms
from django.forms import ModelForm, TextInput, Textarea


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('name', 'title', 'body')
        widgets = {
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
