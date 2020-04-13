import json

from datetime import datetime

from django.contrib import messages
from django.http import (
    HttpResponse,
    HttpResponseBadRequest,
    HttpResponseNotFound,
)
from django.shortcuts import (
    redirect,
    render,
    get_object_or_404,
)
from django.urls import reverse

from .forms import CarouselForm
from .models import CarouselImage
from skka.settings import TZ, NAME

def handler400(request, exception=None):
    return render(request, 'home/400.html', status=400)

def handler403(request, exception=None):
    return render(request, 'home/403.html', status=403)

def handler404(request, exception=None):
    return render(request, 'home/404.html', status=404)

def handler500(request, exception=None):
    return render(request, 'home/500.html', status=500)

def index(request):
    return render(request, 'home/index.html', {
        'images': CarouselImage.objects.all().order_by('date_updated'),
        'year': datetime.now(TZ).year,
        'name': NAME,
    })

def carousel_manager(request):
    if request.method != 'GET':
        return HttpResponseBadRequest()

    return render(request, 'home/carousel_manager.html', {
        'images': CarouselImage.objects.all().order_by('date_updated'),
        'year': datetime.now(TZ).year,
        'name': NAME,
    })

def carousel_upload(request):
    if request.method == 'GET':
        return render(request, 'home/carousel_upload.html', {
            'form': CarouselForm(),
            'year': datetime.now(TZ).year,
            'name': NAME,
        })
    elif request.method == 'POST':
        form = CarouselForm(request.POST, request.FILES)

        if form.is_valid():
            images = request.FILES.getlist('images')
            for img in images:
                image = CarouselImage.create(image=img)
                image.save()

            images_len = len(images)
            messages.success(request, 'You have successfully added %d image%s to the carousel. <a href="%s">Click here</a> to see the updated carousel.' % (images_len, '' if images_len == 1 else 's', reverse('home:index')), extra_tags='safe')

            return redirect('home:carousel-upload')

        messages.error(request, 'There was an error adding the image to the carousel.')

        return redirect('home:carousel-upload')

    return HttpResponseBadRequest()

def carousel_reorder(request):
    if request.method != 'GET':
        return HttpResponseBadRequest()

    # retrieve lists
    order = json.loads(request.GET.get('order'))
    images = CarouselImage.objects.all()

    # validate input
    for img in images:
        if img.id not in order:
            messages.error(request, 'There was an error reordering the carousel images. At least one of the images specified could not be found.')

            return HttpResponseNotFound()

    # touch images in order
    for img_id in order:
        CarouselImage.objects.get(id=img_id).save()

    messages.success(request, 'You have successfully reordered the carousel images. <a href="%s">Click here</a> to see the updated carousel.' % reverse('home:index'), extra_tags='safe')

    return HttpResponse(status=200)

def carousel_delete(request, img_id):
    if request.method != 'GET':
        return HttpResponseBadRequest()

    img = get_object_or_404(CarouselImage, id=img_id)
    img.delete()

    messages.success(request, 'You have successfully deleted the carousel image.')

    return redirect('home:carousel')

def about(request):
    if request.method != 'GET':
        return HttpResponseBadRequest()

    return render(request, 'home/about.html', {
        'year': datetime.now(TZ).year,
        'name': NAME,
    })
