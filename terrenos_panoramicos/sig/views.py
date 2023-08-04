from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

import json
from django.core.serializers import serialize
from django.views.generic.base import TemplateView


class MarkersMapView(TemplateView):
    template_name = "sig/map.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        geo_data =[]
        geojson = serialize("geojson", geo_data)
        print(geojson)
        context["geo_data"] = json.loads(geojson)
        return context


def view_all_geographical_properties(request):
    properties = []
    print(properties)
    return render(
        request,
        "sig/view_all_properties.html",
        {"properties": properties, "nombres": ["Axel", "Mel"]},
    )
