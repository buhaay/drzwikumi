from pprint import pprint

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm
import os
import re

static_images = settings.DOOR_IMAGES

description = {
    'Virage': [
        'Skrzydło wykonane w technologii ramiakowej',
        'Ramiaki pionowe wykonane z płyty MDF o szerokości 140mm pokryte okleiną',
        'Płyciny wykonane z płyty MDF o grubości 16mm pokryte okleiną',
        'Okucia: 3 zawiasy czopowe',
        'Zamek: zasuwkowy, oszczędnościowy, pod wkładkę patentową lub z blokadą',
        'Szyba dekormat, bezpieczna przeźroczysta 3.3.1 lub bezpieczna mleczna 3.3.1'
    ],
    'Evri': [
        'Skrzydło wykonane w technologii ramiakowej',
        'Ramiaki pionowe wykonane z płyty MDF o szerokości 140mm pokryte okleiną',
        'Płyciny wykonane z płyty MDF o grubości 4mm pokryte okleiną',
        'Okucia: 3 zawiasy czopowe',
        'Zamek: zasuwkowy, oszczędnościowy, pod wkładkę patentową lub z blokadą',
        'Szyba dekormat',
    ],
    'River': [
        'Skrzydło wykonane w technologii ramiakowej',
        'Ramiaki pionowe wykonane z płyty MDF lub z klejonki iglastej obłożone płytą HDF,'
        'o szerokości 140mm pokryte okleiną',
        'Ramiaki poziome wykonane z płyty MDF o grubości 22mm pokryte okleiną',
        'Okucia: 3 zawiasy czopowe',
        'Zamek: zasuwkowy, oszczędnościowy, pod wkładkę patentową lub z blokadą',
        'Szyba dekormat',
    ]
}


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))


def offer_main(request):
    context = {
        'examples': [],
    }
    main_dir = '{}/{}'.format(static_images, 'maindoors')
    for root, directories, files in os.walk(main_dir):
        for directory in directories:
            files = os.listdir('{}/{}'.format(main_dir, directory))
            context['examples'].append({'name': directory,
                                        'image': sorted(files)[0]})
    pprint(context)
    return render(request, 'offer_main.html', context)


def door_details(request, door_name):
    files = os.listdir('{}/{}/{}'.format(static_images, 'maindoors', door_name.capitalize()))

    main = {
        'src': files[0],
        'color': files[0].split('-')[1].capitalize()
    }

    images = []
    for file in files:
        color = file.split('-')[1]
        if color.startswith('4'):
            color = ''
            main = {'src': file, 'color': ''}
        if 'dab' in color:
            result = re.search('(dab)(\w+)', color)
            color = '{} {}'.format(result.group(1).replace('a', 'ą'),
                                   result.group(2))
        elif 'orzechciemny' in color.lower():
            result = re.search('(orzech)(\w+)', color, re.I)
            color = '{} {}'.format(result.group(1),
                                   result.group(2))
        elif 'machon' in color.lower():
            color = color.replace('n', 'ń')
        elif 'bialy' in color.lower():
            color = color.replace('l', 'ł')
        elif 'wisnia' in color.lower():
            color = color.replace('s', 'ś')

        images.append({'src': file, 'color': color.capitalize()})

    context = {
        'images': images,
        'main': main,
        'door_name': door_name,
    }
    return render(request, 'door_details_main.html', context)


def offer_room(request):
    context = {
        'examples': [],
    }

    main_dir = '{}/{}'.format(static_images, 'roomdoors')
    for directory in os.listdir(main_dir):
        example_dir = {
            'name': directory,
            'series': [],
        }
        for serie in os.listdir('{}/{}'.format(main_dir, directory)):
            if os.path.isdir('{}/{}/{}'.format(main_dir, directory, serie)):
                files = os.listdir('{}/{}/{}'.format(main_dir, directory, serie))
                example = files[0]
                if example.startswith('k'):
                    example = files[1]
                example_dir['series'].append({
                    'serie': serie,
                    'image': example,
                })
        context['examples'].append(example_dir)
    return render(request, 'offer_room.html', context)


def room_details(request, door_name, door_series):
    files = os.listdir('{}/{}/{}/{}'.format(static_images, 'roomdoors',
                                            door_name.capitalize(), door_series))

    images = []
    for file in files:
        if file.startswith('kolory'):
            color = file
        else:
            images.append({'src': file})

    main = {'src': images[0]['src']}

    context = {
        'images': images,
        'main': main,
        'door_name': door_name,
        'series': door_series,
        'color': color,
        'descriptions': description[door_name],
    }

    return render(request, 'door_details_room.html', context)


def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render({}, request))


def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = '\n\r'.join(['Od: {}'.format(from_email),
                                   'Wiadomość: {}'.format(form.cleaned_data['message'])])
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, ['drzwikumi@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request, 'index.html', {})
    return render(request, "contact.html", {'form': form})
