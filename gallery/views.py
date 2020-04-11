from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponseBadRequest

from .models import GalleryImage
from skka.settings import TZ, NAME

def index(request):
    if request.method != 'GET':
        return HttpResponseBadRequest()

    images_by_category = []
    for category_id, name in GalleryImage.CATEGORY_CHOICES:
        images = GalleryImage.objects.filter(category=category_id)

        if images:
            images_by_category.append({
                'id': category_id,
                'name': name,
                'images': images,
            })

    return render(request, 'gallery/index.html', {
        'images_by_category': images_by_category,
        'year': datetime.now(TZ).year,
        'name': NAME,
    })

def manager(request):
    if request.method != 'GET':
        return HttpResponseBadRequest()

    images_by_category = []
    for category_id, name in GalleryImage.CATEGORY_CHOICES:
        images = GalleryImage.objects.filter(category=category_id)

        if images:
            images_by_category.append({
                'id': category_id,
                'name': name,
                'images': images,
            })

    return render(request, 'gallery/manager.html', {
        'images_by_category': images_by_category,
        'year': datetime.now(TZ).year,
        'name': NAME,
    })
