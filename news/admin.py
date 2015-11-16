from django.contrib import admin
from news.models import New
from news.models import PhotoOfWeek


class PhotoOfWeekAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Nazev fotky', {'fields': ['title']}),
        ('Text fotky', {'fields': ['text']}), 
        ('Fotka tydne', {'fields': ['image']}),
    ]
    list_display = ('id', 'title', 'text', 'image')
    #list_filter = ['date']    # date neni v puvodnim navrhu DB - upravovat ?
    search_fields = ['title', 'text']



class NewAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Nadpis', {'fields': ['title']}),
        ('Text novinky', {'fields': ['text']}),
	('Links', {'fields': ['link1', 'link1_name', 'link2', 'link2_name',
                              'link3', 'link3_name', 'link4', 'link4_name'
                             ], 'classes': ['collapse']}),
        ('Obrazky', {'fields': ['image1', 'image1_name', 'image2', 'image2_name',
                                'image3', 'image3_name', 'image4', 'image4_name'
                             ], 'classes': ['collapse']}),
    ]
    list_display = ('id', 'title', 'date')
    list_filter = ['date']
    search_fields = ['title', 'text', 
                     'link1_name', 'link2_name', 'link3_name', 'link4_name',
                     'image1_name', 'image2_name', 'image3_name', 'image4_name']



# Register your models here ###############################

admin.site.register(New, NewAdmin)
admin.site.register(PhotoOfWeek, PhotoOfWeekAdmin)
#admin.site.register(New)
#admin.site.register(PhotoOfWeek)


