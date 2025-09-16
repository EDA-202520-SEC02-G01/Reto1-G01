import time
import csv
import sys

csv.field_size_limit(2147483647)
default_limit = 1000
sys.setrecursionlimit(default_limit*10)

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    catalogo={"pickup_datetim":[],"dropoff_datetime":[],"passenger_count":[],"trip_distance":[],"pickup_longitude":[],"pickup_latitude":[],"rate_code":[],"dropoff_longitude":[],"dropoff_latitude":[],"payment_type":[],"fare_amount":[],"extra":[],"mta_tax":[],"tip_amount":[],"tolls_amount":[],"improvement_surcharg":[],"total_amount":[]}
    return catalogo

# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    archivo=open(filename,"r")
    titulos=archivo.readline()
    linea=archivo.readline()
    while len(linea)>0:
        datos=linea.split(",")
        catalog["pickup_datetim"].append(datos[1])
        catalog["dropoff_datetime"].append(datos[2])
        catalog["passenger_count"].append(datos[3])
        catalog["trip_distance"].append(datos[4])
        catalog["pickup_longitude"].append(datos[5])
        catalog["pickup_latitude"].append(datos[6])
        catalog["rate_code"].append(datos[7])
        catalog["dropoff_longitude"].append(datos[8])
        catalog["dropoff_latitude"].append(datos[9])
        catalog["payment_type"].append(datos[10])
        catalog["fare_amount"].append(datos[11])
        catalog["extra"].append(datos[12])
        catalog["mta_tax"].append(datos[13])
        catalog["tip_amount"].append(datos[14])
        catalog["tolls_amount"].append(datos[15])
        catalog["improvement_surcharg"].append(datos[16])
        catalog["total_amount"].append(datos[17])
        linea=archivo.readline()
    archivo.close
    return catalog
        

# Funciones de consulta sobre el catálogo

def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Consulta en las Llamar la función del modelo para obtener un dato
    pass


def req_1(catalog):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(catalog):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(catalog):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
