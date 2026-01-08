# ¿Qué es el Scraping?
#"Es una técnica que usa Python para extraer información de sitios web de forma automática y organizada."
import requests 

url = "https://www.google.com/"
response = requests.get(url)
print("-- REPORTE DE SCRAPING --")
print(f"Sitio visitado: {url}")
print(f"Estado de la conexion: {response.status_code}")
print(f"Tamaño del contenido: {len(response.text)} caractreres")