from flask import Flask, render_template
import geopandas as panda
import folium

app = Flask(__name__)

@app.route('/')
def index():
    # Cargar mapa con GeoPandas desde archivos Shape
    gdf = panda.read_file('data/peru.shp')

    # Crear un mapa de Folium
    m = folium.Map(location=[-9.1900, -75.0152], zoom_start=6)

    # Agregar la capa de imágenes mundiales de Esri con la atribución predeterminada
    folium.TileLayer(
        tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        name='Esri World Imagery',
        overlay=True,
        attr='Esri World Imagery'
    ).add_to(m)

    # Agregar los datos GeoJSON al mapa
    folium.GeoJson(gdf).add_to(m)

    # Pintar nuestra plantilla
    return render_template('index.html', map=m._repr_html_())

if __name__ == '__main__':
    app.run(debug=True)
