from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import *

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