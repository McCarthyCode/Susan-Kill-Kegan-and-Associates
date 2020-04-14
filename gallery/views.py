import json

from datetime import datetime

from django.contrib import messages
from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
    reverse,
)
from django.http import (
    HttpResponse,
    HttpResponseBadRequest,
    HttpResponseNotFound,
)

from .models import GalleryImage
from .forms import GalleryForm
from skka.settings import TZ, NAME

def index(request):
    if request.method != 'GET':
        return HttpResponseBadRequest()

    images_by_category = []
    for category_id, name in GalleryImage.CATEGORY_CHOICES:
        images = GalleryImage.objects.filter(category=category_id).order_by('date_updated')

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
    if not (request.method == 'GET' and request.user.is_superuser):
        return HttpResponseBadRequest()

    images_by_category = []
    for category_id, name in GalleryImage.CATEGORY_CHOICES:
        images = GalleryImage.objects.filter(category=category_id).order_by('date_updated')

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
    if not request.user.is_superuser:
        return HttpResponseBadRequest()

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

def reorder(request):
    if not (request.method == 'GET' and request.user.is_superuser):
        return HttpResponseBadRequest()

    # retrieve lists
    orders = json.loads(request.GET.get('orders'))

    # validate input
    for category in orders:
        for img in GalleryImage.objects.filter(category=category['id']):
            if img.id not in category['order']:
                messages.error(request, 'There was an error reordering the gallery images. At least one of the images specified could not be found.')

                return HttpResponseNotFound()

    # touch images in order
    for category in orders:
        for img_id in category['order']:
            img = GalleryImage.objects.get(id=img_id).save()

    messages.success(request, 'You have successfully reordered the gallery images. <a href="%s">Click here</a> to see the updated gallery.' % reverse('gallery:index'), extra_tags='safe')

    return HttpResponse(status=200)

def delete(request, img_id):
    if not (request.method == 'GET' and request.user.is_superuser):
        return HttpResponseBadRequest()

    img = get_object_or_404(GalleryImage, id=img_id)
    img.delete()

    messages.success(request, 'You have successfully deleted the gallery image.')

    return redirect('gallery:manager')
