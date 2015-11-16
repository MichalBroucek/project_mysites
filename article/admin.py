from django.contrib import admin
from article.models import Article
from article.models import Category

# Register your models here.
admin.site.register(Article)
admin.site.register(Category)
