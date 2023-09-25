# Proyecto de Datos Geoespaciales con Python


## Estructura del proyecto
app.py: El archivo principal de la aplicación Flask.

templates/: Carpeta que contiene las plantillas HTML.

static/: Carpeta que contiene archivos estáticos como CSS, JavaScript, y recursos de Leaflet.

data/: Carpeta que contiene datos geoespaciales en formato Shapefile u otros formatos compatibles con GeoPandas.

## Personalización
Puedes personalizar la aplicación editando el archivo app.py y las plantillas HTML en la carpeta templates. Además, puedes agregar tus propios datos geoespaciales en la carpeta data.

## Proyecto Flask
Este proyecto utiliza las siguientes tecnologías y bibliotecas:

- [Folium](https://python-visualization.github.io/folium/): Biblioteca de visualización de mapas interactivos.
- [Leaflet](https://leafletjs.com/): Biblioteca de JavaScript para mapas interactivos.
- [Flask](https://flask.palletsprojects.com/): Marco web de Python para la creación de aplicaciones web.
- [GeoPandas](https://geopandas.org/): Biblioteca de Python para el análisis y visualización de datos geoespaciales.

## Configuración del Entorno

Para configurar el entorno de desarrollo, sigue estos pasos:

1. Crea un entorno virtual de Python:

python -m venv venv


2. Activa el entorno virtual (en Windows):

venv\Scripts\activate

3. instala las librerias de Python

pip install flask foliuma geopandas Leaflet

3.1 en nuestro caso ya lo realizamos solo tenemos que instalar los requerimientos con el siguiente comando

pip install -r requirements.txt

## Ejecución
Para ejecutar la aplicación, utiliza el siguiente comando:


python app.py


La aplicación estará disponible en http://127.0.0.1:5000/. Puedes acceder a ella desde tu navegador web.
