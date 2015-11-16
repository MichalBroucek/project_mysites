from django.conf.urls import patterns, include, url
from messages import views

urlpatterns = patterns('',
    url(r'^$', views.messages, name='messages'),
    url(r'^new/$', views.new_message, name='new_message'),
    url(r'^receive_message/$', views.receive_message, name='receive_message'),
)

