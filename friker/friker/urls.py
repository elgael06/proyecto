
from django.contrib import admin
from django.urls import path, include, re_path

from photos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', views.home),
    re_path(r'^about/$', views.about),
    re_path(r'^login/$', views.login),
    re_path(r'^usuarios/$', views.usuarios),

]
