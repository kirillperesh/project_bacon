from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import *
from .forms import *

def home(request):
    return render(
        request,
        'lmae/base.html',
        {            
            'date': datetime.now()
        }
    )

def base(request, name):
    return render(
        request,
        'lmae/base.html',
        {
            'name': name,
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

def db_smth(request):
    form_set = PersonFormSet(queryset=Person.objects.none())


    return render(
        request,
        'lmae/db_smth.html',
        {
            'form_set': form_set,    
            'date': datetime.now()
        }
    )
