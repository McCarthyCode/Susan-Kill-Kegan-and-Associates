from django import forms
from django.contrib.auth.models import User

from .models import CarouselImage

class UserForm(forms.Form):
    username = forms.CharField(
        label='',
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username',
        }),
    )
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password',
        })
    )

class CarouselForm(forms.ModelForm):
    images = forms.ImageField(
        label='Images',
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
    )

    def clean(self):
        super().clean()
        return self.cleaned_data

    class Meta:
        model = CarouselImage
        fields = ['image']
