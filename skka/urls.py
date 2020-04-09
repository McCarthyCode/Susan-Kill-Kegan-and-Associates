"""skka URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path, include
from django.conf.urls import (
    handler400,
    handler403,
    handler404,
    handler500,
)
from django.conf.urls.static import static

from skka.settings import DEBUG, MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    re_path(r'^', include(('home.urls', 'home'), namespace='home')),
    re_path(r'^gallery/', include(('gallery.urls', 'gallery'), namespace='gallery')),
    re_path(r'^admin/', admin.site.urls),
]

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

handler400 = 'home.views.handler400'
handler403 = 'home.views.handler403'
handler404 = 'home.views.handler404'
handler500 = 'home.views.handler500'
