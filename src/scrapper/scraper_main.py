import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
from ..decorator.decorator_main import time_analysis, log_analysis

##
# @brief Esta función permite validar antes de ejecutar el scraping que la pagina a ser procesada se encuentre en linea
# @param url La url de la pagina a ser procesada
# @return True si la pagina se encuentra en linea, False en caso contrario
##
@log_analysis
@time_analysis
def valid_page_for_scrape(base_url):
    response= requests.get(base_url) # Realizamos una solicitud GET para comprobar que la página se encuentre OK
    if response.status_code == 200:
        return True
    else:
        print(Exception(f"Failed to fetch page: {base_url}")) 
        return False

##
# @brief Esta función permite leer una página web (inicialmente testeada),
# de la cual conocemos que su navegación entre productos depende del scrolling del usuario.
# Para lo cual, hacemos uso del paquete Selenium para realizar la simulacion de la navegación.
# @param url La dirección de la página web que se va a leer.
# @return La composición BeautifulSoup de la pagina consultada.
#
##
@log_analysis
@time_analysis
def initialization_scrape(base_url, driver):
    valid_page = valid_page_for_scrape(base_url)

    if valid_page:
        driver.get(base_url) # Abrimos la página en el navegador usando el driver
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "productVitrine"))) 
        initial_html = driver.page_source # Se obtiene la pagina a fin de 
        initial_soup = BeautifulSoup(initial_html, "html.parser")

        #Obtener el número total de productos de la página especifica
        total_productos = float(initial_soup.select_one(".value").get_text(strip=True))
        print(f"La cantidad total de productos a obtener es: {total_productos}")

        return total_productos
    else:
        return 0

##
# @brief Esta función permite descomponer los campos Nombre/Titulo y Precio del producto.
# Para luego crear un listado con los datos obtenidos de la página, usando un ciclo para navegar entre los items disponibles.
# @param soup La composición BeautifulSoup de la pagina consultada, con los registros a descomponer.
# @return lista de productos.
##
@log_analysis
@time_analysis
def process_datahtml_to_list(items):
    data = []
    for item in items:
        name_element = item.select_one("a") # Selector para el nombre del producto
        price_element = item.select_one(".price") # Selector para el precio del producto

        if name_element and price_element:
            name = name_element["title"] # Extraer nombre de la clase title
            price = price_element.get_text(strip=True) # Extraer precio del producto
            data.append({"title": name, "price": price})

        if not name_element or not price_element:
            continue
    return data


##
# @brief Esta función permite navegar entre las páginas de la tienda en línea.
# @param driver El driver de Selenium que se utiliza para navegar.
# @param scroll_count Cantidad total de productos disponibles en la página.
# @return La lista de todos los productos que se obtuvieron de la página (Cantidad Total de Productos).
##
@log_analysis
@time_analysis
def execute_simulate_scroll(scroll_count, driver):
    # Obtenemos el largo de la página
    last_height = driver.execute_script("return document.body.scrollHeight")
    products = [] # Creamos variable temporal que alojara los productos que vamos obteniendo del scanning de la página
    while scroll_count > len(products):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
        initial_html = driver.page_source
        initial_soup = BeautifulSoup(initial_html, "html.parser")
        items = initial_soup.select(".productVitrine")
        products = process_datahtml_to_list(items)

    # Close the WebDriver
    driver.quit()
    # Return products
    return products

def list_to_pd_and_save(productos):
    df = pd.DataFrame(productos)
    df.to_csv('data/raw/scraper_products.csv', index= False) # Guardamos los datos en un archivo CSV sin incluir el indice.

if __name__ == "__main__":
    base_url = "https://www.pycca.com/tecnologia/audio-y-video"
    driver = webdriver.Chrome()  # Make sure you have chromedriver installed and in your PATH
    count_products = initialization_scrape(base_url, driver)
    products = execute_simulate_scroll(count_products, driver)
    list_to_pd_and_save(products)