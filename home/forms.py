from django import forms

from .models import CarouselImage

class CarouselForm(forms.ModelForm):
    image = forms.ImageField(
        label='Image',
        widget=forms.ClearableFileInput(),
    )

    def clean(self):
        super().clean()
        return self.cleaned_data

    class Meta:
        model = CarouselImage
        fields = ['image']
