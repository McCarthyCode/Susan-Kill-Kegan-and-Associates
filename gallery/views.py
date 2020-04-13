from datetime import datetime

from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest

from .models import GalleryImage
from .forms import GalleryForm
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

def upload(request):
    if request.method == 'GET':
        return render(request, 'gallery/upload.html', {
            'form': GalleryForm(),
            'year': datetime.now(TZ).year,
            'name': NAME,
        })
    elif request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)

        if form.is_valid():
            img_form = form.save(commit=False)

            images = request.FILES.getlist('images')
            category = img_form.category
            for img in images:
                image = GalleryImage.create(image=img, category=category)
                image.save()

            images_len = len(images)
            messages.success(request, 'You have successfully added %d image%s to the gallery.' % (images_len, '' if images_len == 1 else 's'))

            return redirect('gallery:upload')

        messages.error(request, 'There was an error adding the image to the gallery.')

        return redirect('gallery:upload')

    return HttpResponseBadRequest()
