from bs4 import BeautifulSoup  # Importamos al 'traductor' de HTML
import requests

url = "https://www.google.com/"
response = requests.get(url)
# Solo ejecutamos el análisis si la página nos dio permiso (Código 200)
if response.status_code == 200:
    print("-- REPORTE DE SCRAPING CON BEAUTIFUL SOUP --")
    print(f"Sitio visitado: {url}")
    print(f"Estado de la conexion: {response.status_code}")
    # Convertimos el texto bruto en una 'sopa' ordenada para poder navegarla
    soup = BeautifulSoup(response.text, 'html.parser')
    # Buscamos la etiqueta <title> directamente en el árbol de la web
    title_tag = soup.title
    if title_tag:
        # .text limpia las etiquetas y nos deja solo las palabras del título
        print(f"El título de la página es: {title_tag.text}")
       
    # Subimos al 'padre' del título para encontrar otras etiquetas ocultas (meta)
    # find_all nos devuelve una LISTA con todas las coincidencias
    metas =soup.title.parent.find_all('meta')
    print(metas)
