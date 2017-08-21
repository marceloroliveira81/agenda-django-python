from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.detalhes, name='detalhes'),
    url(r'^novo/$', views.novo, name='novo'),
    url(r'^alterar/(?P<pk>[0-9]+)/$', views.alterar, name='alterar'),
    url(r'^excluir/(?P<pk>[0-9]+)/$', views.excluir, name='excluir'),
]