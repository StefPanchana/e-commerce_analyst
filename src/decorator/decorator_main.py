import time
import logging

##
# Class Decorator_Main
# La presente clase, automatiza la validacion de tiempo de ejecucion y loggin de las funciones que se desean analizar.
# A continuacion se definen los formatos a usar para los registros, incluidas las marcas de tiempo, el respectivo nivel del mensaje
# y la composición del mensaje a visualizar.
##

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

##
# Decorador para medir el tiempo de ejecución de una función
##
def time_analysis(func):
    def wrapper(*args, **kwargs):
        init_time = time.time()  # Registra el inicio de la llamada al decorador
        result = func(*args, **kwargs)  # Ejecuta la función que emplea el decorador
        end_time = time.time()  # Registra la finalizacion de la llamada al decorador
        elapsed_time = end_time - init_time  # Calcula el tiempo transcurrido
        logging.info(f"{func.__name__} executed in {elapsed_time:.4f} seconds")  # Registra el tiempo de ejecución
        return result 
    return wrapper

##
# Decorador para loggear la ejecución de una función
##
def log_analysis(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Running {func.__name__}")  # Registra el inicio de la llamada al decorador
        result = func(*args, **kwargs)  # Ejecuta la función que emplea el decorador
        logging.info(f"Completed {func.__name__}")  # Registra la finalizacion de la llamada al decorador
        return result 
    return wrapper