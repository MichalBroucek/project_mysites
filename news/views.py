from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

from news.models import New
from news.models import PhotoOfWeek

import string


# Create your views here. #

# More or less static views #################################################

def info(request):
    """Basic info about pages"""
    pictureOfWeek = PhotoOfWeek.objects.last()
    return render(request, 'news/info.html', {'pictureOfWeek': pictureOfWeek})


def kontakt(request):
    """Info about contatct of author"""
    pictureOfWeek = PhotoOfWeek.objects.last()
    return render(request, 'news/kontakt.html', {'pictureOfWeek': pictureOfWeek})


# More or less dynamic views #################################################

def news0_redirect(request):
    """Just redirect URL without parameters to the news/0/ ... the last 10 news"""
    return redirect('news:news', start_id='0')


def news(request, start_id):
    """Short news for info about latest actions"""

    MAX_NEWS = 10
    end_id = string.atoi(start_id) + 10

    news_count = New.objects.count()  # Pocet vsech zaznamu novinek
    news_list = New.objects.all().order_by("-date")[start_id:end_id]  # Sort by date ... and only part of list
    # misto vsech zaznamu ziskat jen ty v intervalu start - stop -> API

    # Vypocet prvniho ID z predchozi skupiny novinek (jedna skupina = MAX_NEWS) 
    start_id_num = string.atoi(start_id)
    if (start_id_num + MAX_NEWS) < news_count:
        preview_start_id = start_id_num + MAX_NEWS
    else:
        preview_start_id = start_id_num

    # Vypocet prvniho ID z nasledujici skupiny novinek (jedna skupina = MAX_NEWS) 
    next_start_id = start_id_num - MAX_NEWS  # prvni ID nasledujicich novinek
    if next_start_id < 0:
        next_start_id = 0;

    pictureOfWeek = PhotoOfWeek.objects.last()
    context = {'news_list': news_list, 'news_count': news_count, 'pictureOfWeek': pictureOfWeek, 'start_id': start_id,
               'preview_start_id': preview_start_id, 'next_start_id': next_start_id}
    return render(request, 'news/news.html', context)


def underConstruction(request):
    """General page to display that page is not finished"""
    pictureOfWeek = PhotoOfWeek.objects.last()
    return render(request, 'underConstruction.html', {'pictureOfWeek': pictureOfWeek})


# def obr1_detail(request, new_id, start_id):
#     """Show detail of picture"""
#     new = New.objects.get(pk=new_id)
#     pictureOfWeek = PhotoOfWeek.objects.last()
#     return render(request, 'news/obr1_detail.html', {'new': new, 'pictureOfWeek': pictureOfWeek, 'start_id': start_id})

# def obr2_detail(request, start_id):
#     """Show detail of picture"""
#     start_id_int = string.atoi(start_id)
#     new = New.objects.get(pk=start_id_int)
#     pictureOfWeek = PhotoOfWeek.objects.last()
#     return render(request, 'news/obr2_detail.html', {'new': new, 'pictureOfWeek': pictureOfWeek, 'start_id': start_id})

# def obr3_detail(request, new_id, start_id):
#     """Show detail of picture"""
#     new = New.objects.get(pk=new_id)
#     pictureOfWeek = PhotoOfWeek.objects.last()
#     return render(request, 'news/obr3_detail.html', {'new': new, 'pictureOfWeek': pictureOfWeek, 'start_id': start_id})

# def obr4_detail(request, new_id, start_id):
#     """Show detail of picture"""
#     new = New.objects.get(pk=new_id)
#     pictureOfWeek = PhotoOfWeek.objects.last()
#     return render(request, 'news/obr4_detail.html', {'new': new, 'pictureOfWeek': pictureOfWeek, 'start_id': start_id})


def obr_detail(request, new_id, start_id, obr_id):
    """
    Show detail of picture
    :param request:
    :param new_id:
    :param start_id:
    :return:
    """
    new = New.objects.get(pk=new_id)
    picture_of_week = PhotoOfWeek.objects.last()
    new_picture_id_list = __get_picture_id_list(new)
    requested_image = __get_requested_image(new, obr_id)
    previous_image = __get_previous_image_id(obr_id, new_picture_id_list)
    next_image = __get_next_image(obr_id, new_picture_id_list)

    parameters = {'new': new, 'pictureOfWeek': picture_of_week, 'start_id': start_id,
                  'requested_image': requested_image, 'previous_image': previous_image, 'next_image': next_image}

    return render(request, 'news/obr_detail.html', parameters)


def __get_picture_id_list(new):
    """
    Return list of ID images which are available for one specific new
    :param new:
    :return: list of images IDs which exists
    """
    id_list = []

    if new.image1:
        id_list.append(1)
    if new.image2:
        id_list.append(2)
    if new.image3:
        id_list.append(3)
    if new.image4:
        id_list.append(4)

    return id_list


def __get_requested_image(new, obr_id):
    """
    Return requested image
    :return:
    """
    # If picture doesn't exist link is not visible on page so don't have to verify if actual picture exists
    if obr_id == "1":
        requested_image = new.image1
    elif obr_id == "2":
        requested_image = new.image2
    elif obr_id == "3":
        requested_image = new.image3
    elif obr_id == "4":
        requested_image = new.image4
    else:
        requested_image = new.image1

    return requested_image


def __get_previous_image_id(obr_id, new_picture_id_list):
    """
    Return reguested image
    :return:
    """
    try:
        actual_id = int(obr_id)  # Exception ?
    except ValueError:
        actual_id = 0

    previous_id = None
    if actual_id - 1 <= 0:
        previous_id = new_picture_id_list[-1]  # Last in the list
    else:
        previous_id_flag = False  # True if next item in reversed list is next picture ID
        for id in reversed(new_picture_id_list):

            if previous_id_flag:  # next item in the reversed list is the previous picture id
                previous_id = id
                break

            if id == actual_id:  # This item is actual picture (next iteration is next picture ID)
                previous_id_flag = True

    return previous_id


def __get_next_image(obr_id, new_picture_id_list):
    """
    Return requested image
    :return:
    """
    try:
        actual_id = int(obr_id)  # Exception ?
    except ValueError:
        actual_id = 0

    next_id = None
    if actual_id >= len(new_picture_id_list):
        next_id = new_picture_id_list[0]  # First in the list
    else:
        next_id_flag = False  # True if next item in list is next picture ID
        for id in new_picture_id_list:

            if next_id_flag:  # next item in the list is the next picture id
                next_id = id
                break

            if id == actual_id:  # This item is actual picture (next iteration is next picture ID)
                next_id_flag = True

    return next_id


def picture_of_day_detail(request, picture_id):
    """Middle section loads picture of the day"""

    pictureBig = PhotoOfWeek.objects.get(pk=picture_id)  # big picture in the middle section (= picture for detail)
    pictureOfWeek = PhotoOfWeek.objects.last()  # small picture on the right panel (always the newest picture)

    all_pictures = PhotoOfWeek.objects.all().order_by("-id")
    temp_picture_id = 0
    count_pictures = len(all_pictures)
    for temp_picture in all_pictures:
        if temp_picture.id == string.atoi(picture_id):
            # Nalezeni predchozi fotky v poradi ##################
            if temp_picture_id < (count_pictures - 1):
                preview_picture = all_pictures[temp_picture_id + 1]
            else:
                preview_picture = all_pictures[count_pictures - 1]
            # Nalezeni nasledujici fotky v poradi ##################
            if temp_picture_id > 0:
                next_picture = all_pictures[temp_picture_id - 1]
            else:
                next_picture = all_pictures[0]

        # Na konci zvyseni indexu znamene presun indexu na starsi fotku (serazeno od nejnovejsi po nejstarsi ...order_by("-date")
        temp_picture_id += 1  # increase id for index in all_pictures array
        # End of for cyklus

    content = {'picture': pictureBig, 'preview_picture_id': preview_picture.id, 'next_picture_id': next_picture.id,
               'pictureOfWeek': pictureOfWeek, }
    return render(request, 'news/picture_of_day.html', content)


def newsList(request):
    """List of all news"""

    news_count = New.objects.count()  # Pocet vsech zaznamu novinek
    news_list = New.objects.all().order_by("date")  # Sort by date ... and only part of list
    # misto vsech zaznamu ziskat jen ty v intervalu start - stop -> API

    pictureOfWeek = PhotoOfWeek.objects.last()
    context = {'news_list': news_list, 'news_count': news_count, 'pictureOfWeek': pictureOfWeek}
    return render(request, 'news/newsList.html', context)


def newsFromList(request, new_db_id):
    """News acording new_db_id (database ID of new)"""
    MAX_NEWS = 10

    news_count = New.objects.count()  # Pocet vsech zaznamu novinek
    news_list_all = New.objects.all().order_by("-date")  # Sort by date ...
    # Z celeho seznamu novinek vybereme jen 10 zacinajici pozadovanym 'new_db_id'
    news_list_part = []
    start_index = 0;
    new_db_id_num = string.atoi(new_db_id)
    for new in news_list_all:
        if new.id == new_db_id_num:
            news_list_part = news_list_all[start_index:start_index + MAX_NEWS]
            break
        start_index = start_index + 1

    # Vypocet prvniho ID z predchozi skupiny novinek (jedna skupina = MAX_NEWS)
    # Poradi je otocene! Posledne zadana novinka je prvni v poradi
    if (start_index + MAX_NEWS) < news_count:
        preview_start_id = start_index + MAX_NEWS
    else:
        preview_start_id = start_index

    # Vypocet prvniho ID z nasledujici skupiny novinek (jedna skupina = MAX_NEWS)
    # Poradi je otocene! Posledne zadana novinka je prvni v poradi
    next_start_id = start_index - MAX_NEWS  # prvni ID nasledujicich novinek
    if next_start_id < 0:
        next_start_id = 0;

    pictureOfWeek = PhotoOfWeek.objects.last()
    context = {'news_list': news_list_part, 'news_count': news_count, 'pictureOfWeek': pictureOfWeek,
               'start_id': start_index, 'preview_start_id': preview_start_id, 'next_start_id': next_start_id}
    return render(request, 'news/news.html', context)


def designTest(request):
    """Short news for info about latest actions"""

    MAX_NEWS = 10
    start_id = '0'
    end_id = string.atoi(start_id) + 10

    news_count = New.objects.count()  # Pocet vsech zaznamu novinek
    news_list = New.objects.all().order_by("-date")[start_id:end_id]  # Sort by date ... and only part of list
    # misto vsech zaznamu ziskat jen ty v intervalu start - stop -> API

    # Vypocet prvniho ID z predchozi skupiny novinek (jedna skupina = MAX_NEWS) 
    start_id_num = string.atoi(start_id)
    if (start_id_num + MAX_NEWS) < news_count:
        preview_start_id = start_id_num + MAX_NEWS
    else:
        preview_start_id = start_id_num

    # Vypocet prvniho ID z nasledujici skupiny novinek (jedna skupina = MAX_NEWS) 
    next_start_id = start_id_num - MAX_NEWS  # prvni ID nasledujicich novinek
    if next_start_id < 0:
        next_start_id = 0;

    pictureOfWeek = PhotoOfWeek.objects.last()
    context = {'news_list': news_list, 'news_count': news_count, 'pictureOfWeek': pictureOfWeek, 'start_id': start_id,
               'preview_start_id': preview_start_id, 'next_start_id': next_start_id}
    return render(request, 'designTest/news_design_test.html', context)
