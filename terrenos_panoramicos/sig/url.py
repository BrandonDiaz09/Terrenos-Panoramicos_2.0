from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.add_geographical_property, name="add_geographical_property"),
]
