from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

from news import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project_mysites.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('news.urls', namespace="news")),
    url(r'^messages/', include('messages.urls', namespace="messages")),
    #url(r'^article/', include('article.urls', namespace="article")),
    url(r'^underConstruction/', views.underConstruction, name='underConstruction'),
    url(r'^design/', views.designTest, name='designTest'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

