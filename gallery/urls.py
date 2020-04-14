from django.urls import re_path

from . import views
from skka.settings import DEBUG

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^manager/$', views.manager, name='manager'),
    re_path(r'^upload/$', views.upload, name='upload'),
    re_path(r'^reorder/$', views.reorder, name='reorder'),
    re_path(r'^delete/(?P<img_id>[1-9]\d*)/$', views.delete, name='delete'),
]
