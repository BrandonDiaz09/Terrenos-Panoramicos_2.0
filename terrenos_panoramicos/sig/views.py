from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

import json
from django.core.serializers import serialize
from django.views.generic.base import TemplateView
import random

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
    import random

    dataInmueble = {
        "datosGenerales": {
            "calle": "Calle Benito Juárez",
            "Numero Oficial": "123",
            "Codigo Postal": "52740",
            "PARAJE": "La Hacienda",
            "NOMBRE DEL POSEEDOR": "María González",
            "USO DE SUELO": "Residencial",
            "SUPERFICIE": "350 m²",
            "MEDIDAS Y COLINDANCIAS":"", 
            "NORTE": "Colinda con propiedad de Juan Martínez",
            "SUR": "Colinda con Calle Morelos",
            "ORIENTE": "Colinda con propiedad de Ana Rodríguez",
            "PONIENTE": "Colinda con propiedad de Carlos López"
            ,
        },
        "datosMedicion": {
            "NORTE": f"{random.randint(100, 300)} metros",
            "SUR": f"{random.randint(100, 300)} metros",
            "ORIENTE": f"{random.randint(100, 300)} metros",
            "PONIENTE": f"{random.randint(100, 300)} metros",
            "SUPERFICIE": f"{random.randint(200, 500)} m²",
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
            "FOTO DEL POSEDOR ACTUAL": "https://images.arq.com.mx/thumbnails/4/244331.jpg"
        },
        "datosGen":{
            "title":"Datos Generales de Medicion",
            "REALIZO": "Axel Diaz",
            "REVISO": "Esteban Medina",
            "Vo. Bo. COMUNEROS": "Jorge Sanchez",
        },
        "Nota": "EL PRESENTE DOCUMENTO Y LOS DATOS CONTENIDOS EN ÉL, SOLO SON DE CARÁCTER TECNICO, POR LO TANTO, NO GENERAN DERECHOS PARA EL O LOS TERRITORIOS DE QUE SE TRATE. DEJANDO A SALVO LOS DERECHOS DE TERCEROS."
    }



    dataState = {
        "type": "Feature",
        "geometry": {
            "type": "Polygon",
            "coordinates": [[
                [-104.05, 48.99],
                [-97.22,  48.98],
                [-96.58,  45.94],
                [-104.03, 45.94],
                [-104.05, 48.99]
            ]]
        }
    }

    return render(
        request,
        "sig/view_all_properties.html", 
        {"dataState":json.dumps(dataState),
        "dataInmueble": dataInmueble},
    )


def owners_list(request):
    import random

    dataList = {
        "Axel": {
            "calle": "Calle Benito Juárez",
            "Numero Oficial": "123",
            "Codigo Postal": "52740",
        },
        "Mel": {
            "calle": "Calle Benito Juárez",
            "Numero Oficial": "123",
            "Codigo Postal": "52740",
        },
        "Bran": {
            "calle": "Calle Benito Juárez",
            "Numero Oficial": "123",
            "Codigo Postal": "52740",
        },
        "Juve": {
            "calle": "Calle Benito Juárez",
            "Numero Oficial": "123",
            "Codigo Postal": "52740",
        },
    }


    return render(
        request,
        "sig/owners_list.html", 
        {"dataState": dataList},
    )
