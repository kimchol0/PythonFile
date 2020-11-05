from django.urls import path, re_path, include
from . import views

urlpatterns = [
    re_path(r'^$', views.index_view),
    re_path(r'^upload/$', views.upload_view),
    re_path(r'^showall/$', views.showall_view),
]
