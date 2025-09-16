import time
import csv
import sys
import datetime

csv.field_size_limit(2147483647)
default_limit = 1000
sys.setrecursionlimit(default_limit*10)

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

def trans_datos(catalog):
    catalog["pickup_datetime"] = datetime.strptime(catalog["pickup_datetime"], "%Y-%m-%d %H:%M:%S")
    catalog["dropoff_datetime"] = datetime.strptime(catalog["dropoff_datetime"], "%Y-%m-%d %H:%M:%S")
    catalog["passenger_count"] = int(catalog["passenger_count"])
    catalog["trip_distance"] = float(catalog["trip_distance"])
    catalog["rate_code"]=int(catalog["rate_code"])
    catalog["extra"]=float(catalog["extra"])
    catalog["mta_tax"]=float(catalog["mta_tax"])
    catalog["tip_amount"] = float(catalog["tip_amount"])
    catalog["tolls_amount"] = float(catalog["tolls_amount"])
    catalog["improvement_surcharge"]=float(catalog["improvement_surcharge"])
    catalog["total_amount"] = float(catalog["total_amount"])
       
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
    trayecto_menordis=[datos["pickup_datetime"][posmenor],dismenordatos["total_amount"][posmenor]]
    trayecto_mayordis=[datos["pickup_datetime"][posmayor],dismayor, datos["total_amount"][posmayor]]
    primeros_5t={"pickup_datetime":datos["pickup_datetime"][0:6],"dropoff_datetime":datos["dropoff_datetime"][0:6],"trip_distance":datos["trip_distance"][0:6],"":[]}


def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    catalogo={"pickup_datetim":[],"dropoff_datetime":[],"passenger_count":[],"trip_distance":[],"pickup_longitude":[],"pickup_latitude":[],"rate_code":[],"dropoff_longitude":[],"dropoff_latitude":[],"payment_type":[],"fare_amount":[],"extra":[],"mta_tax":[],"tip_amount":[],"tolls_amount":[],"improvement_surcharg":[],"total_amount":[]}
    return catalogo

# Funciones para la carga de datos

def req_1(catalog, pasajeros):
    """
    Retorna el resultado del requerimiento 1
    """
    catalog=trans_datos(catalog)
    inicio=get_time()
    res={}
    conteo_fecha={}
    propina=0
    cuenta_mediopago={}
    peajes=0
    distancia=0
    tiempo=0
    costo_total=0
    cuentapasajeros=0 
    for i in range(0,len(catalog["passenger_count"])):
        if catalog["passenger_count"][i]== pasajeros:
            cuentapasajeros+=1
            duracion=catalog["dropoff_datetime"][i]-catalog["pickup_datetime"][i]
            tiempo+=duracion
            costo_total+=catalog["total_amount"][i]
            distancia+=catalog["trip_distance"][i]
            peajes+=catalog["tolls_amount"][i]
            modo_pago=catalog["payment_type"][i]
            cuenta_mediopago[modo_pago]=cuenta_mediopago.get(modo_pago,0)+1
            propina+=catalog["tip_amount"]
            fecha=catalog["pickup_datetime"][i].date()
            conteo_fecha[fecha]=conteo_fecha.get(fecha,0)+1
                   
    tiempo=tiempo/cuentapasajeros
    tiempo=tiempo.total_seconds()/60
    costo_total=costo_total/cuentapasajeros
    distancia=distancia/cuentapasajeros
    peajes=peajes/cuentapasajeros
    mayor=max(cuenta_mediopago, key=cuenta_mediopago.get)
    mas_usado= f"{mayor} - {cuenta_mediopago[mayor]}"
    propina=propina/cuentapasajeros
    mas_frecuente=max(conteo_fecha,key=conteo_fecha.get)
    fecha_inicio_max= f"{mas_frecuente} - {conteo_fecha[mas_frecuente]}"


          
    res["filtro de pasajeros"]=cuentapasajeros
    res["promedio de tiempo"]=tiempo  
    res["promedio de costoTotal"]=costo_total 
    res["distancia promedio"]=distancia
    res["promedio pagos en peajes"]=peajes
    res["medio de pago mas usado"]=mas_usado
    res["promedio de propina"]=propina
    res["fecha de inicio con mayor frecuencia"]=fecha_inicio_max
    final=get_time()
    tiempo=delta_time(inicio,final)
    res["tiempo"]=tiempo
    
    return res 
    

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
