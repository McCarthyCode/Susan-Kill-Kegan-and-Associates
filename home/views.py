from datetime import datetime

from django.contrib import messages
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect

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
        'images': CarouselImage.objects.all().order_by('-date_updated'),
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
            image = form.save()
            image.image_ops()
            image.save()

            messages.success(request, 'You have successfully added an image to the carousel.')

            return redirect('home:carousel-upload')

        messages.error(request, 'There was an error adding the image to the carousel.')

        return redirect('home:carousel-upload')

    return HttpResponseBadRequest()
