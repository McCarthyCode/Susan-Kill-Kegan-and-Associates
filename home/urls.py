from django.urls import re_path

from . import views
from skka.settings import DEBUG

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^carousel/$', views.carousel_manager, name='carousel'),
    re_path(r'^carousel/upload/', views.carousel_upload, name='carousel-upload'),
]

if DEBUG:
    urlpatterns += [
        re_path(r'^400/$', views.handler400),
        re_path(r'^403/$', views.handler403),
        re_path(r'^404/$', views.handler404),
        re_path(r'^500/$', views.handler500),
    ]
