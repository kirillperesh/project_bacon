from django.forms import modelformset_factory
from .models import *

PersonFormSet = modelformset_factory(Person, fields=('first_name', 'last_name'), extra=2)

# import inspect, sys, importlib
# for name, cls in inspect.getmembers(importlib.import_module("lmae.models"), inspect.isclass):
#     print(cls)