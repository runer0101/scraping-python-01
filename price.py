from bs4 import BeautifulSoup  # Importamos al 'traductor' de HTML
import requests

url = "https://www.amazon.com/-/es/AMD-Procesador-desbloqueado-RyzenTM-9600X/dp/B0D6NN6TM7/?_encoding=UTF8&pd_rd_w=8Tnl1&content-id=amzn1.sym.4bba068a-9322-4692-abd5-0bbe652907a9&pf_rd_p=4bba068a-9322-4692-abd5-0bbe652907a9&pf_rd_r=KHVYPFB179QBNNXHTFPC&pd_rd_wg=GMPcF&pd_rd_r=243b0f5e-1f65-46d4-a236-8118e3960a70&ref_=pd_hp_d_btf_nta-top-picks"

# Una manera de hacer scrapin a los navegadores que tienen seguridad anti-bots especifica es 'fingir' ser un navegador real
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
       
    # Buscamos el precio usando su id único
    price_span = soup.find('span', class_='rc-prices-full-price')
    if price_span:
        print(f"El precio del producto es: {price_span.text.strip()}")
    else:
        print("No se pudo encontrar el precio del producto.")