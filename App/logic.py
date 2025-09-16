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
        for i in range(0,len(titulos)):
            datos=linea.split(",")
            catalog[titulos[i]].append(datos[i])
        linea=archivo.readline()
    archivo.close
    return catalog
        
def reporte(catalog, filename):
    inicio=get_time()
    datos=load_data(catalog, filename)
    final=get_data()
    tiempo=delta_time(inicio,final)
    for columnas in datos.keys():
        if columnas=="trip_distance":
            dismayor=datos[columnas][0]
            posmayor=0
            dismenor=datos[columnas][0]
            posmenor=0
            for i in range(0,datos[columnas]):
                dis=datos[columnas][i]
                if dismenor>dis:
                    dismenor=dis
                    posmenor=i
                if dismayor<dis:
                    dismayor=dis
                    posmayor=i
    trayecto_menordis=[datos["pickup_datetime"][posmenor],dismenor, datos["total_amount"][posmenor]]
    trayecto_mayordis=[datos["pickup_datetime"][posmayor],dismayor, datos["total_amount"][posmayor]]
    primeros_5t={"pickup_datetime":datos["pickup_datetime"][0:6],"dropoff_datetime":datos["dropoff_datetime"][0:6],"trip_distance":datos["trip_distance"][0:6],"":[] }
                
                

# Funciones de consulta sobre el catálogo

def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    dic={}
    for columnas in catalog.key():
        dic[columnas]=catalog[columnas][id]
    return dict


def req_1(catalog):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(catalog,medio):
    """
    Retorna el resultado del requerimiento 2
    """
    #funcar
    inicio=get_time()
    cantidad=0
    costo=1
    distancia=0
    pedajes=0
    cantidad_pasajeros={}
    mayor=0
    propina=0
    cantidad_finalizacion={}
    tiempo=0
    for i in range(0,len(catalog["payment_type "])):
        if catalog["payment_type "][i]==medio:
            cantidad+=1
            costo+=catalog["total_amount"][i]
            distancia+=catalog["trip_distance"][i]
            pedajes+=catalog["tolls_amount"][i]
            cantidad_pasajeros[catalog["passenger_count"][i]]=cantidad_pasajeros.get(catalog["passenger_count"][i],0)+1
            cantidad_finalizacion=[catalog["dropoff_datetime"][i].date()]=cantidad_finalizacion.get(catalog["dropoff_datetime"][i].date(),0)+1
            catalog["dropoff_datetime"].date()
            if cantidad==1:
                mayor=catalog["passenger_count"][i]
                repetido=catalog["dropoff_datetime"][i].date()
            elif cantidad_pasajeros[catalog["passenger_count"][i]]>cantidad_pasajeros[mayor]:
                mayor=catalog["passenger_count"][i]
            elif cantidad_finalizacion[catalog["dropoff_datetime"].date()]>cantidad_finalizacion[repetido]:
                repetido=catalog["dropoff_datetime"].date()
            propina+=catalog["tip_amount"][i]
            tiempo+=(catalog["dropoff_datetime"][i]-catalog["pickup_datetime"][i])
    dic={"num_trayectos":cantidad,"tiempo_promedio":tiempo/cantidad,"costo_promedio":costo/cantidad,"pasajeros_frec":str(mayor)+" - "+str(cantidad_pasajeros[mayor]),"propina_promedio":propina/cantidad,"fecha_mas trayectos":repetido}
    final=get_time()
    tiempo=delta_time(final,inicio)
    dic["Tiempo"]=tiempo
    return dic
    
    
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

