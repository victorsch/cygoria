from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^contact/', views.contact, name='contact'),
	url(r'^news/', views.news, name='news'),
	url(r'^analysis/', views.analysis, name='analysis'),
]
