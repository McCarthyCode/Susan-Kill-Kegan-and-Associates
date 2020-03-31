from django.urls import path, re_path

from . import views
from skka.settings import DEBUG

urlpatterns = [
    path('', views.index, name='index'),
]

if DEBUG:
    urlpatterns += [
        re_path(r'^400/', views.handler400),
        re_path(r'^403/', views.handler403),
        re_path(r'^404/', views.handler404),
        re_path(r'^500/', views.handler500),
    ]
