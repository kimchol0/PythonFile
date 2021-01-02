from django.urls import path, re_path, include
from . import views

urlpatterns = [
    re_path(r'^$', views.index_view),
    re_path(r'^upload/$', views.upload_view),
    re_path(r'^showall/$', views.showall_view),
    re_path(r'^download/$', views.download_view),
    re_path(r'^redirect/$', views.index_view2),
    re_path(r'^showallRedirect/$', views.showallRedirect_view),
    re_path(r'^login/$', views.login_view),
    re_path(r'^main/$', views.main),
]
