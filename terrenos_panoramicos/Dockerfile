# Uso de Python 3.8.0 como imagen base
FROM python:3.8.0

# Instalación de dependencias necesarias
RUN apt-get update && apt-get install -y \
    binutils \
    libproj-dev \
    gdal-bin \
    libgdal-dev

# Configuración del directorio de trabajo
RUN mkdir /code
WORKDIR /code

# Configuración de variables de entorno para Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instalación de dependencias de Python
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Instalación específica de GDAL para asegurar la compatibilidad
RUN pip install GDAL==$(gdal-config --version) --global-option=build_ext --global-option="-I/usr/include/gdal"

# Copia del código fuente
COPY . /code

# Verificación de los archivos en el directorio de trabajo
RUN ls -la /code

# Configuración del script de entrada
COPY entrypoint.sh /code/
RUN chmod +x /code/entrypoint.sh
ENTRYPOINT ["/code/entrypoint.sh"]
