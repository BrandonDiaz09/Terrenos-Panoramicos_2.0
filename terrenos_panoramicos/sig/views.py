from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

import json
from django.core.serializers import serialize
from django.views.generic.base import TemplateView
import random
from ventas.models import Inmueble


class MarkersMapView(TemplateView):
    template_name = "sig/map.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        geo_data = []
        geojson = serialize("geojson", geo_data)
        print(geojson)
        context["geo_data"] = json.loads(geojson)
        return context


def view_all_geographical_properties(request):
    import random

    try:
        inmueble_mas_actual = Inmueble.objects.latest("created")
        datos_generales = inmueble_mas_actual
        perimetro_queryset = []
        return render(
            request,
            "403.html",
            {},
        )
    except Inmueble.DoesNotExist:
        # Manejar la situación en la que no hay inmuebles en la base de datos
        return render(
            request,
            "403.html",
            {},
        )
    imagenes = {
        "UBICACIÓN EN MUNICIPIO": inmueble_mas_actual.ubicacion_en_municipio.url
        if inmueble_mas_actual.ubicacion_en_municipio
        else "",
        "CROQUIS DE UBICACIÓN": inmueble_mas_actual.croquis_de_ubicacion.url
        if inmueble_mas_actual.croquis_de_ubicacion
        else "",
        "CROQUIS DEL PREDIO": inmueble_mas_actual.croquis_de_del_predio.url
        if inmueble_mas_actual.croquis_de_del_predio
        else "",
        "FOTO DEL PREDIO": inmueble_mas_actual.foto_del_predio.url
        if inmueble_mas_actual.foto_del_predio
        else "",
        "ORTOFOTO": inmueble_mas_actual.ortofoto.url
        if inmueble_mas_actual.ortofoto
        else "",
        "FOTO DEL POSEDOR ACTUAL": inmueble_mas_actual.foto_de_posedor_actual.url
        if inmueble_mas_actual.foto_de_posedor_actual
        else "",
    }
    dataInmueble = {
        "datosGenerales": {
            "calle": inmueble_mas_actual.street,
            "Numero Oficial": inmueble_mas_actual.number_of,
            "Codigo Postal": inmueble_mas_actual.postal_code,
            "PARAJE": inmueble_mas_actual.paraje,
            "NOMBRE DEL POSEEDOR": inmueble_mas_actual.user.username,
            "USO DE SUELO": inmueble_mas_actual.get_uso_suelo_display(),
            "SUPERFICIE": f"{inmueble_mas_actual.surface} m²",
            "MEDIDAS Y COLINDANCIAS": "",
            "NORTE": f"{colindancias_prop.norte} metros",  # Agregar la información real aquí
            "SUR": f"{colindancias_prop.sur} metros",  # Agregar la información real aquí
            "ORIENTE": f"{colindancias_prop.este} metros",  # Agregar la información real aquí
            "PONIENTE": f"{colindancias_prop.oeste} metros",  # Agregar la información real aquí
        },
        "imagenes": imagenes,
        "datosTerra": {
            "title": "Datos Generales de Medicion",
            "NORTE": f"{colindancias_tv.norte} metros",
            "SUR": f"{colindancias_tv.sur} metros",
            "ORIENTE": f"{colindancias_tv.este} metros",
            "PONIENTE": f"{colindancias_tv.oeste} metros",
            "SUPERFICIE": f"{inmueble_mas_actual.surface} m²",
            "NOMBRE DEL ACTUAL POSEEDOR": f"{inmueble_mas_actual.user.username}",
            "NOMBRE DEL ACTUAL POSEEDOR": "Eduardo Ramírez",
        },
        "detallePago": {
            "TOTAL A PAGAR": f"${random.randint(10000, 50000)}",
            "OBSERVACIONES": "Sin observaciones",
        },
        "imagenes": {
            "UBICACIÓN EN MUNICIPIO": "https://static.vecteezy.com/system/resources/previews/001/061/391/non_2x/architectural-blueprints-and-blueprint-rolls-with-drawing-instruments-photo.jpg",
            "CROQUIS DE UBICACIÓN": "https://images.arq.com.mx/thumbnails/4/244331.jpg",
            "CROQUIS DEL PREDIO": "https://marvich.cl/wp-content/uploads/2019/11/94911bdd6640f0dba85c698d13a7e900.gif",
            "FOTO DEL PREDIO": "https://images.arq.com.mx/thumbnails/4/244331.jpg",
            "ORTOFOTO": "https://topografiaygeosistemas.com/wp-content/uploads/2015/05/plano-topografico.jpg",
            "FOTO DEL POSEDOR ACTUAL": "https://images.arq.com.mx/thumbnails/4/244331.jpg",
        },
        "datosGen": {
            "title": "Datos Generales de Medicion",
            "REALIZO": "Axel Diaz",
            "REVISO": "Esteban Medina",
            "Vo. Bo. COMUNEROS": "Jorge Sanchez",
        },
        "Nota": "EL PRESENTE DOCUMENTO Y LOS DATOS CONTENIDOS EN ÉL, SOLO SON DE CARÁCTER TECNICO, POR LO TANTO, NO GENERAN DERECHOS PARA EL O LOS TERRITORIOS DE QUE SE TRATE. DEJANDO A SALVO LOS DERECHOS DE TERCEROS.",
    }

    return render(
        request,
        "sig/view_all_properties.html",
        {
            "dataState": json.dumps(dataState),
            "dataInmueble": dataInmueble,
        },
    )


def owners_list(request):
    dataList = {
        "Axel": {
            "calle": "Calle Benito Juárez",
            "numero_oficial": "123",
            "codigo_postal": "52740",
        },
        "Mel": {
            "calle": "Calle Benito Juárez",
            "numero_oficial": "123",
            "codigo_postal": "52740",
        },
        "Bran": {
            "calle": "Calle Benito Juárez",
            "numero_oficial": "123",
            "codigo_postal": "52740",
        },
        "Juve": {
            "calle": "Calle Benito Juárez",
            "numero_oficial": "123",
            "codigo_postal": "52740",
        },
    }


    return render(
        request,
        "sig/owners_list.html", 
        {"dataList": dataList},
    )
