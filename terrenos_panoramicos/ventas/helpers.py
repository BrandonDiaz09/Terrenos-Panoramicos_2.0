from math import atan2, degrees, sqrt
from .helpers import calculate_distance, calculate_bearing, calculate_rumbo

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


def create_shapefile_records(all_points, transformer):
    records = []
    if not all_points:
        return records

    # Record inicial
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

    # Procesar cada punto para crear records
    for i in range(len(all_points) - 1):
        point1, point2 = all_points[i], all_points[i + 1]
        distance = calculate_distance(point1, point2)
        bearing = calculate_bearing(point1, point2)
        rumbo = calculate_rumbo(bearing)
        lat1, lon1 = point2[1], point2[0]
        record = {
            "EST": f"{i + 1}",
            "PV": f"{i + 2}",
            "RUMBO": rumbo,
            "DISTANCIA": distance,
            "V": f"{i + 2}",
            "X": lon1,
            "Y": lat1,
        }
        records.append(record)

    # Record final
    point1, point2 = all_points[-1], all_points[0]
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
        "Y": lat1,
    }
    records.append(record_end)

    return records