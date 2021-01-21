from django.forms import modelformset_factory
from .models import *

PersonFormSet = modelformset_factory(Person, fields=('first_name', 'last_name'), extra=2)