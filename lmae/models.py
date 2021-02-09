from django.db import models


class City(models.Model):
    city_name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

    @classmethod
    def get_default_city(cls):
        return cls.objects.get_or_create(city_name='*unknown')

    @classmethod
    def get_deleted_city(cls):
        return cls.objects.get_or_create(city_name='*DELETED')

    def __str__(self):
        return f"{self.city_name} ({self.country})"

class Person(models.Model):
    GENDERS = [
    ('M', 'Male'),
    ('W', 'Female'),
    ('Mi-24', 'Attack Helicopter'),
    ('n/a', 'Not sure'),
    ]
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=10, choices=GENDERS, default='n/a')
    city = models.ForeignKey(City, null=True, default=None, on_delete=City.get_deleted_city, related_name='person')

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.gender}, {self.city}"

def get_all_models(names = False):
    import inspect
    import sys
    if names:
        return [name for name, cls in inspect.getmembers(sys.modules[__name__], inspect.isclass)]
    return [cls for name, cls in inspect.getmembers(sys.modules[__name__], inspect.isclass)]

def get_model(*, model_name):
    import sys
    return getattr(sys.modules[__name__], model_name)
