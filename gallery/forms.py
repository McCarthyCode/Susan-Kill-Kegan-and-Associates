from django import forms

from .models import GalleryImage

class GalleryForm(forms.ModelForm):
    images = forms.ImageField(
        label='Image',
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
    )

    category = forms.ChoiceField(
        label='Category',
        choices=GalleryImage.CATEGORY_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    def clean(self):
        super().clean()
        cleaned_data = self.cleaned_data

        cleaned_data['category'] = int(cleaned_data['category'])

        return cleaned_data

    class Meta:
        model = GalleryImage
        fields = ['image', 'category']
