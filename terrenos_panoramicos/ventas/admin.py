import tempfile
from django.contrib.gis import admin
from ventas.models import Inmueble
from .forms import InmuebleForm
import shapefile
import os
from math import atan2, degrees, sqrt
from pyproj import Proj, Transformer
from sig.models import ConstructionFrame, ConstructionPoint
from django.contrib.gis.geos import Point

def calculate_polygon_area(coordinates):
    n = len(coordinates)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += coordinates[i][0] * coordinates[j][1]
        area -= coordinates[j][0] * coordinates[i][1]
    area = abs(area) / 2.0
    return area

# Funciones de cálculo
def calculate_distance(point1, point2):
    return sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def calculate_bearing(point1, point2):
    angle_rad = atan2(point2[1] - point1[1], point2[0] - point1[0])
    angle_deg = degrees(angle_rad)
    bearing = (angle_deg + 360) % 360
    return bearing

def decimal_to_dms(decimal_degrees):
    degrees = int(decimal_degrees)
    minutes_full = (decimal_degrees - degrees) * 60
    minutes = int(minutes_full)
    seconds = (minutes_full - minutes) * 60
    return (degrees, minutes, seconds)

def calculate_rumbo(bearing):
    """
    Convert a bearing angle in degrees to the traditional surveying notation.

    :param bearing: Bearing in degrees from the North line clockwise.
    :return: Bearing in the surveying format.
    """
    if 0 <= bearing < 90:
            d, m, s = decimal_to_dms(90 - bearing)
            return f"N {d:02d}°{m:02d}'{s:05.2f}\" E"
    elif 90 <= bearing < 180:
        d, m, s = decimal_to_dms(bearing - 90)
        return f"N {d:02d}°{m:02d}'{s:05.2f}\" W"
    elif 180 <= bearing < 270:
        d, m, s = decimal_to_dms(270 - bearing)
        return f"S {d:02d}°{m:02d}'{s:05.2f}\" W"
    elif 270 <= bearing < 360:
        d, m, s = decimal_to_dms(bearing - 270)
        return f"S {d:02d}°{m:02d}'{s:05.2f}\" E"
    else:
        raise ValueError("Bearing must be between 0 and 360 degrees.")

@admin.register(Inmueble)
class InmuebleAdmin(admin.ModelAdmin):
    form = InmuebleForm
    list_display = ("pk", "profile","surface", "front", "bottom", "status")
    list_display_links = ("pk", "profile")
    list_editable = ("surface", "front", "bottom", "status")
    search_fields = (
        "status",
        "regimen_propiedad",
        "uso_suelo",
    )

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
            extra_context = extra_context or {}
            print(object_id)
            inmueble = self.model.objects.get(pk=object_id) if object_id else None
            # Verifica si ya hay ConstructionFrame relacionados
            has_construction_frames = inmueble.construction_frame.exists() if inmueble else False
            print(has_construction_frames)
            # Pasar el contexto a la plantilla para controlar la visibilidad del botón
            extra_context['has_construction_frames'] = has_construction_frames
            return super().changeform_view(request, object_id, form_url, extra_context=extra_context)
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        shapefile = form.cleaned_data.get('shapefile')
        if shapefile:
            self.process_shapefile(shapefile, obj)

    
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
            transformer = Transformer.from_crs("EPSG:32614", "EPSG:4326", always_xy=True)
            all_points = [shape.points[0] for shape in sf.shapes()]
            # all_points = [(shape.points[i][0], shape.points[i][1]) for shape in sf.shapes() for i in range(len(shape.points))]
            print(f"Todos los puntos son {len(all_points)} y tiene {sf.shapes()}")
            records = []
            record_init = {
                "EST": "",
                "PV": "",
                "RUMBO": "",
                "DISTANCIA": "",
                "V": "1",
                "X": all_points[0][0] if all_points[0] is not None else "",
                "Y": all_points[0][1] if all_points[0] is not None else "",
            }
            records.append(record_init)
    
            for i in range(len(all_points) - 1):
                point1, point2 = all_points[i], all_points[i + 1]
                distance = calculate_distance(point1, point2)
                bearing = calculate_bearing(point1, point2)
                rumbo = calculate_rumbo(bearing)
                lat1, lon1 = point2[1], point2[0]
                record = {
                    "EST": f"{i + 1}", # or whatever value is appropriate for 'EST'
                    "PV": f"{i + 2}", # or whatever value is appropriate for 'PV'
                    "RUMBO": rumbo,
                    "DISTANCIA": distance,
                    "V": f"{i + 2}", # or the appropriate value for 'V'
                    "X": lon1,
                    "Y": lat1
                }
                records.append(record)
            point1, point2 =  all_points[-1],all_points[0]
            distance = calculate_distance(point1, point2)
            bearing = calculate_bearing(point1, point2)
            rumbo = calculate_rumbo(bearing)
            lat1, lon1 = point2[1], point2[0]
            record_end = {
                "EST": f"{len(all_points)}",
                "PV": "1",
                "RUMBO": rumbo,
                "DISTANCIA": distance,
                "V": "1",
                "X": lon1,
                "Y": lat1
            }
            records.append(record_end)

            construction_frame, created = ConstructionFrame.objects.get_or_create(inmueble=inmueble)
            print(records)
            print(len(records))
            # Borra FramePoints antiguos si es necesario
            if not created:
                construction_frame.construction_points.all().delete()
            for record in records:
                print("--")
                print(record)
                print("--")

                # Asumiendo que 'X' y 'Y' son coordenadas longitud y latitud respectivamente
                lon, lat = transformer.transform(float(record['X']), float(record['Y']))
                point_location = Point(lon, lat, srid=4326)  # SRID 4326 = WGS84
                frame_point = ConstructionPoint(
                    construction_frame=construction_frame,
                    est=record['EST'] if record['EST'] != "" else None,
                    pv=record['PV'] if record['PV'] != "" else None,
                    rumbo=record['RUMBO'] if record['RUMBO'] != "" else None,
                    distancia=record['DISTANCIA'] if record['DISTANCIA'] != "" else None,
                    v=record['V'] if record['V'] != "" else None,
                    point=point_location
                )
                frame_point.save()
                print(f"Construccion Frames y sus Frames {frame_point}")