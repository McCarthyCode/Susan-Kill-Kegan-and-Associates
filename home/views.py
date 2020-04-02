from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

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
        'year': datetime.now(TZ).year,
        'name': NAME,
    })
