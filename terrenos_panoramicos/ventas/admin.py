import tempfile
from django.contrib.gis import admin
from ventas.models import Inmueble
from .forms import InmuebleForm
import shapefile
import os
from math import atan2, degrees, sqrt
from pyproj import Proj, transform
from sig.models import ConstructionFrame

# Esta función debe recibir dos tuplas o listas de coordenadas: (x1, y1) y (x2, y2)
def calculate_distance(point1, point2):
    return sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)


def calculate_bearing(point1, point2):
    angle_rad = atan2(point2[1] - point1[1], point2[0] - point1[0])
    angle_deg = degrees(angle_rad)
    bearing = (angle_deg + 360) % 360
    return bearing

def calculate_rumbo(bearing):
    # Convertir el rumbo en grados a formato de grados, minutos y segundos
    # Esto es un esquema básico, necesitarías ajustarlo para tus necesidades específicas
    degrees = int(bearing)
    minutes = int((bearing - degrees) * 60)
    seconds = (bearing - degrees - minutes/60) * 3600
    return f"N {degrees}°{minutes}'{seconds:.2f}\" E"

@admin.register(Inmueble)
class InmuebleAdmin(admin.ModelAdmin):
    form = InmuebleForm
    list_display = ("pk", "user", "surface", "front", "bottom", "status")
    list_display_links = ("pk", "user")
    list_editable = ("surface", "front", "bottom", "status")
    search_fields = (
        "user__email",
        "user__first_name",
        "user__last_name",
        "status",
        "regimen_propiedad",
        "uso_suelo",
    )

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
            extra_context = extra_context or {}
            print(object_id)
            inmueble = self.model.objects.get(pk=object_id) if object_id else None
            # Verifica si ya hay ConstructionFrame relacionados
            has_construction_frames = inmueble.construction_frames.exists() if inmueble else False
            print(has_construction_frames)
            # Pasar el contexto a la plantilla para controlar la visibilidad del botón
            extra_context['has_construction_frames'] = has_construction_frames
            return super().changeform_view(request, object_id, form_url, extra_context=extra_context)
    # def save_model(self, request, obj, form, change):
    #     super().save_model(request, obj, form, change)
    #     shapefile = form.cleaned_data.get('shapefile')
    #     if shapefile:
    #         self.process_shapefile(shapefile, obj)

    
    def process_shapefile(self, shapefile_file, inmueble):
        # Crea un directorio temporal para guardar los archivos del Shapefile
        with tempfile.TemporaryDirectory() as tmpdirname:
            # Guarda el archivo subido en el directorio temporal
            shp_path = os.path.join(tmpdirname, "shapefile.shp")
            with open(shp_path, 'wb') as tmp_shp:
                for chunk in shapefile_file.chunks():
                    tmp_shp.write(chunk)

            # Lee el Shapefile
            sf = shapefile.Reader(shp_path)
            
            # Suponiendo que tienes un sistema de coordenadas proyectadas y deseas convertir a WGS84
            # Deberías conocer el sistema de coordenadas de tu Shapefile para hacer esto
            in_proj = Proj('epsg:6372')  # Reemplaza 'XXXX' con el EPSG adecuado
            out_proj = Proj('epsg:4326')  # WGS84

            points = [(shape.points[i][0], shape.points[i][1]) for shape in sf.shapes() for i in range(len(shape.points))]
            for i in range(len(points) - 1):
                distance = calculate_distance(points[i], points[i+1])
                # El resto de tu código sigue aquí...
                bearing = calculate_bearing(points[i], points[i+1])
                rumbo = calculate_rumbo(bearing)

                # Transforma las coordenadas X, Y a latitud y longitud
                lat, lon = (points[i][0], points[i][1])

                # Crea una instancia del modelo
                frame = ConstructionFrame(
                    est=i+1,
                    pv=i+2,
                    rumbo=rumbo,
                    distancia=distance,
                    v=i+1,  # Suponiendo que 'v' es el índice del punto
                    lat=lat,
                    long=lon,
                    inmueble=inmueble,
                )
                frame.save()
                print(f"Distancia {distance} Rumbo {rumbo}  {lat} {lon} {i+1} {i+2} ")