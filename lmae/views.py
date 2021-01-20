from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import *

def home(request):
    return HttpResponse("Hello, Django!")

def base(request, name):

    if '_' in name:
        name_list = name.split('_', 1)
        new_person = Person.objects.create(first_name=name_list[0], last_name=name_list[1])
    else:        
        new_person = Person.objects.create(first_name=name)

    return render(
        request,
        'lmae/base.html',
        {
            'name': new_person,
            'date': datetime.now()
        }
    )

def base_create(request):
    return render(
        request,
        'lmae/base_create.html',
        {            
            'date': datetime.now()
        }
    )

def budget_edit(request):
    return render(
        request,
        'lmae/budget_edit.html',
        {            
            'date': datetime.now()
        }
    )