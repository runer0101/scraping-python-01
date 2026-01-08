from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
 
def scrape_url(url: str):
 headers = {
   'User-Agent': 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/131.0.0 Safari/537.36'
 }
 response = requests.get(url, headers=headers)
 
 if response.status_code == 200:
   print('La petición fue exitosa')
 
   soup = BeautifulSoup(response.text, 'html.parser')
 
   # Extraer todos los titulos h1
   titulos = [titulo.string for titulo in soup.find_all('h1')]
   print(titulos)
 
scrape_url('https://midu.dev') 