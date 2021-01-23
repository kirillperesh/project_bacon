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

def db_all(request):    

    titles = dict()
    data = dict()
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



# data = dict()
# field_names = dict()
# for model in get_all_models():    
#     field_names[model.__name__] = [f.name for f in list(model._meta.get_fields())]
    
#     #data[model.__name__] = [[getattr(ins, name) for name in field_names[model.__name__]] for ins in model.objects.prefetch_related().all()]


# print(field_names[City.__name__])

# for ins in City.objects.prefetch_related().all():
#     for name in field_names[City.__name__]:
#         print(getattr(ins, name), end=' ')
#     print('\n')
