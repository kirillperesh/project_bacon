from datetime import datetime
from django.shortcuts import render
# from django.http import HttpResponse
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

def db_all(request):
    titles = dict()
    data = dict()
    field_names = dict()
    for model in get_all_models():
        titles[model.__name__] = [f.verbose_name for f in list(model._meta.get_fields())]
        field_names[model.__name__] = [f.name for f in model._meta.get_fields()]
        data[model.__name__] = [[getattr(ins, name) for name in field_names] for ins in model.objects.prefetch_related().all()]

    return render(
        request,
        'lmae/db_all.html',
        {
            'titles': titles,
            'data': data,
            'date': datetime.now()
        }
    )

def db_add(request, table_name=''):
    context = dict()

    if not table_name:
        context = {'tables_list': get_all_models(names=True)}
    else:
        #context = {'tables_list': [get_model(model_name=table_name).objects.all(),]}
        form_set = get_form_set(model_name=table_name)(queryset=get_model(model_name=table_name).objects.none())
        context = {'tables_list': [form_set,]}

    return render(
        request,
        'lmae/db_add.html', context
    )
