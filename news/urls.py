from django.conf.urls import patterns, include, url
from news import views

urlpatterns = patterns('',
    # Redirect to news/0/ ... last 10 news
    url(r'^$', views.news0_redirect, name='news0Redirect'),
    url(r'^(?P<start_id>\d+)/$', views.news, name='news'),
    url(r'^newsFromList/(?P<new_db_id>\d+)/$', views.newsFromList, name='newsFromList'),
    #url(r'^news/$', views.news, name='news'),    
    url(r'^(?P<start_id>\d+)/news_obr1_detail/(?P<new_id>\d+)/$', views.obr1_detail, name='obr1_detail'),
    url(r'^(?P<start_id>\d+)/news_obr2_detail/(?P<new_id>\d+)/$', views.obr2_detail, name='obr2_detail'),
    url(r'^(?P<start_id>\d+)/news_obr3_detail/(?P<new_id>\d+)/$', views.obr3_detail, name='obr3_detail'),
    url(r'^(?P<start_id>\d+)/news_obr4_detail/(?P<new_id>\d+)/$', views.obr4_detail, name='obr4_detail'),
    url(r'^pictureOfWeekDetail/(?P<picture_id>\d+)/$', views.picture_of_day_detail, name='picture_of_week_detail'),
    url(r'^info/$', views.info, name='info'),
    url(r'^kontakt/$', views.kontakt, name='kontakt'),
    url(r'^newsList/$', views.newsList, name='newsList'),
)

