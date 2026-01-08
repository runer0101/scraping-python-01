from bs4 import BeautifulSoup  # Importamos al 'traductor' de HTML
import requests

url = "https://www.apple.com/es/shop/buy-mac/macbook-air/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}
response = requests.get(url, headers=headers)
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
       
    # Buscamos todos los precios de productos en la página
    products = soup.find_all(class_='rc-prroductselection-item')
    for product in products:
        name = product.find(class_='list-title').text
        price = product.find(class_="rc-prices-fullprice").text
        print(f"Producto: {name} - Precio: {price}") 