from django.conf.urls import patterns, include, url
from article import views

urlpatterns = patterns('',
    url(r'^$', views.article, name='article'),
)

