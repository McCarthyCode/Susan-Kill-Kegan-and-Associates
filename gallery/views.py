from django.shortcuts import render
from django.http import (
    HttpResponse,
    # HttpResponseBadRequest,
    # HttpResponseNotFound,
)

def index(request):
    return HttpResponse('Gallery')
