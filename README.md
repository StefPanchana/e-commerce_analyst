## Proyecto E-Commerce_Analyst: Scraping de Productos
# Este proyecto realiza un scraping de productos de un sitio web, para luego limpiar, analizar datos para posterior guardar los resultados en archivo CSV.
# Creado por: Gloria Stefania Panchana Jaramillo

# Advice
El presente metodo de scraper tiene la peculiaridad de ejecutarse sobre una página que se basa en scrolling para mostrar productos.
Por tal motivo, el presente proyecto, realiza una simulaciòn de scroll automatico. Para lo cual es necesario que antes de ejecutar el proyecto confirmemos que
tenemos instalado el browser Chrome de Google.

# Requisitos.

*   Python 3.11+
*   requests
*   selenium
*   pandas
*   beautifulsoup4
*   jupyterlab
*   seaborn
*   matplotlib
*   pygwalker
*   nbconvert

# Requisitos Previos para instalación de dependencias
# VirtualEnv

Se sugiere crear un entorno virtual haciendo uso de virtualenv para la ejecución del presente proyecto, a fin de no alterar ninguna dependencia de su entorno local.

- Comando:

*   pip install virtualenv

- Creación de Ambiente Virtual

*   virtualenv <env_name>

- Activación del Ambiente Virtual

*   <env_name>\Scripts\activate

- Desactivación del Ambiente Virtual

*   deactivate

# Instalación de Dependencias

Una vez hemos creado y activado nuesto ambiente virtual, se procede a instalar los requerimientos del presente proyecto:

*   pip install -r .\requirements.txt

# Estructura del Proyecto

    e-commerce-analyst
    |-- data/
    |   |- raw/
    |       |__ scraper_products.csv
    |   |- processed/
    |       |__ cleaned_products.csv
    |-- notebooks/
    |   |__ abalysis_data.ipynb
    |
    |-- src/
    |   |- process/
    |       |__ __init__.py
    |       |__ process_main.py
    |   |- decorator/
    |       |__ __init__.py
    |       |__ decorator_main.py
    |   |- scrapper/
    |       |__ __init__.py
    |       |__ scrapper_main.py
    |__ README.md
    |__ requirements.txt

# Ejecución del Scraper.

Antes de iniciar tener en cuenta lo descrito en el apartado "Advice", del presente README.md

-   Primera Fase:
-   Ejecutar el siguiente comando para la simulación de scroll por el usuario en base al total de articulos disponibles en la página y obtención de los mismos. 
*   python -m src.scrapper.scraper_main

-   Segunda Fase:
-   Ejecutar el siguiente comando para la lectura del archivo CSV, depuración y análisis previo de datos.
*   python -m src.process.process_main

-   Tercera Fase:
-   Ejecutar el notebook que realiza la categorización del campo Precio a fin de mejorar las visualizaciones presentadas según el análisis realizado a los datos.