from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import GeographicalPropertyForm
from sig.models import GeographicalProperty
import json
from django.core.serializers import serialize
from django.views.generic.base import TemplateView


class MarkersMapView(TemplateView):
    template_name = "sig/map.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        markers = GeographicalProperty.objects.all()
        geojson = serialize("geojson", markers)
        print(geojson)
        context["markers"] = json.loads(geojson)
        return context


def add_geographical_property(request):
    if request.method == "POST":
        form = GeographicalPropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("nombre-de-tu-url")
    else:
        form = GeographicalPropertyForm()

    return render(request, "sig/test.html", {"form": form})


def view_all_geographical_properties(request):
    properties = GeographicalProperty.objects.all()
    print(properties)
    return render(
        request,
        "sig/view_all_properties.html",
        {"properties": properties, "nombres": ["Axel", "Mel"]},
    )
