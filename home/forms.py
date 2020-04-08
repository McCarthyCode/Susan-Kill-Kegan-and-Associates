from django import forms

from .models import CarouselImage

class CarouselForm(forms.ModelForm):
    images = forms.ImageField(
        label='Image',
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
    )

    def clean(self):
        super().clean()
        return self.cleaned_data

    class Meta:
        model = CarouselImage
        fields = ['image']
