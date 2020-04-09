from django.urls import re_path

from . import views
from skka.settings import DEBUG

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^carousel/$', views.carousel_manager, name='carousel'),
    re_path(r'^carousel/upload/', views.carousel_upload, name='carousel-upload'),
    re_path(r'^carousel/reorder/', views.carousel_reorder, name='carousel-reorder'),
    re_path(r'^carousel/delete/(?P<img_id>[1-9]\d*)/', views.carousel_delete, name='carousel-delete'),
    re_path(r'^about/$', views.about, name='about'),
]

if DEBUG:
    urlpatterns += [
        re_path(r'^400/$', views.handler400),
        re_path(r'^403/$', views.handler403),
        re_path(r'^404/$', views.handler404),
        re_path(r'^500/$', views.handler500),
    ]
