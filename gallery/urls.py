from django.urls import re_path

from . import views
from skka.settings import DEBUG

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^manager/$', views.manager, name='manager'),
    re_path(r'^upload/$', views.upload, name='upload'),
]
