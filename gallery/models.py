from django.db import models

from home.models import ThumbnailedImage

class GalleryImage(ThumbnailedImage):
    CATEGORY_CHOICES = [
        (0, 'Residential'),
        (1, 'Commercial'),
        (2, 'Schools'),
        (3, 'Enhancements'),
        (4, 'Sustainability'),
    ]

    category = models.PositiveSmallIntegerField(choices=CATEGORY_CHOICES)

    def relative_path(instance, filename):
        return 'gallery/%s/%s' % (instance.CATEGORY_CHOICES[instance.category][1].lower(), filename)

    image = models.ImageField(blank=True, null=True, default=None, upload_to=relative_path)
    thumbnail = models.ImageField(blank=True, null=True, default=None, upload_to=relative_path)

    def image_ops(self):
        super().image_ops(
            relative_path=self.relative_path(''), max_size=(800, 600)
        )
