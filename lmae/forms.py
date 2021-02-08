from django.forms import modelformset_factory
from .models import *


PersonFormSet = modelformset_factory(Person, exclude=('',), extra=1)
CityFormSet = modelformset_factory(City, exclude=('',), extra=1)

def get_form_set(*, model_name):
    import sys
    return getattr(sys.modules[__name__], f"{model_name}FormSet")
