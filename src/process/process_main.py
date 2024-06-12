import pandas as pd
import os
import itertools
from ..decorator.decorator_main import time_analysis, log_analysis

##
# @brief Función que permite cargar los productos de una archivo .CSV
# @param Ruta del archivo local
# @return Dataframe con productos.
##
@log_analysis
@time_analysis
def load_data(file_path):
    df = pd.read_csv(file_path)
    print("Loading Sucessfull")
    return df

##
# @brief Función permite limpiar la columna precio del simbolo ($) y cambia el tipo de dato de la columna a float.
# @param Dataframe a limpiar.
# @return Dataframe limpio.
##
@log_analysis
@time_analysis
def clean_data(df):
    # Limpiar columna de precios, simbolo de dolar y cambio de tipo de dato
    df["price"] = df["price"].replace("[$,]", "", regex=True)
    df['price'] = df['price'].astype(float)

    print("Data cleaned successfully")  
    return df 

##
# @brief Función que presenta un análisis de los registros obtenidos del scraper realizado.
# @param Dataframe que se analizara.
# @output Información de los registros presentes.
##
@log_analysis
@time_analysis
def data_analysis(df):
    # Presentar informe general del dataframe
    print("Cantidad de registros Registros-Columnas:")
    print(df.shape)

    print("Sumario de la información obtenida: ")
    print(df.describe())

    # Verificar porcentaje de valores nulos en el dataframe
    print(f"El porcentaje de nulos en el dataframe es: \n{df.isnull().sum().sort_values(ascending=False) / len(df) * 100}")

    # Presentar los productos contenidos en el dataframe
    print("Lista de productos del dataframe:")
    keyGroup = [keys.lower().split(', ') for keys in df['title']]
    for key in keyGroup:
        print(f"Productos Encontrados: {key}")

    # Presentar de la columna precio, los siguientes parámetros:
    # Media, Desviación Estandar, Maximo
    print(f"Media: {df['price'].mean()}")
    print(f"Desviación Estandar: {df['price'].std()}")
    print(f"Precio Máximo: {df['price'].max()}")

##
# @brief Función que guarda en un archivo .CSV los productos luego de realizada la limpieza de registros.
# @param Dataframe con registros y ruta de salida del archivo .CSV con registros depurados.
# @output Archivo .CSV generado.
##
@log_analysis
@time_analysis
def save_data_clean(df, output_path):
    df.to_csv(output_path, index=False)  # Guarda los datos en un archivo CSV sin índice

if __name__ == "__main__":
    data_path = "data/raw/scraper_products.csv"  # Define la ruta del archivo de datos
    output_path = "data/processed/cleaned_products.csv"  # Define la ruta del archivo de datos limpios

    df = load_data(data_path)
    df_clean = clean_data(df)
    data_analysis(df_clean)
    os.makedirs("/data/processed", exist_ok=True)
    save_data_clean(df_clean, output_path)