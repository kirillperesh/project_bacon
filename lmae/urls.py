from django.urls import path
from lmae import views

urlpatterns = [
    path("", views.home, name="home"),
    path("base/<name>", views.base, name="base"),
    path("create", views.base_create, name="create"),
    path("budget_edit", views.budget_edit, name="budget_edit"),
    path("db_smth", views.db_smth, name="db_smth"),
]