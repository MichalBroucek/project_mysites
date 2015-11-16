from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

from news.models import PhotoOfWeek

# Create your views here.

def article(request):
    """Article view page """
    pictureOfWeek = PhotoOfWeek.objects.last()
    context = {'pictureOfWeek': pictureOfWeek}
    return render(request, 'articles/article.html', context)

    
