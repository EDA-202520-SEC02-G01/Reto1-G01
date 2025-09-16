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
    inicio=get_time()
    catalog=trans_datos(catalog)
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
    
    inicio=get_time()
    catalog=trans_datos(catalog)
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
            cantidad_finalizacion=[catalog["dropoff_datetime"][i]]=cantidad_finalizacion.get(catalog["dropoff_datetime"][i],0)+1
            if cantidad==1:
                mayor=catalog["passenger_count"][i]
                repetido=catalog["dropoff_datetime"][i]
            elif cantidad_pasajeros[catalog["passenger_count"][i]]>cantidad_pasajeros[mayor]:
                mayor=catalog["passenger_count"][i]
            elif cantidad_finalizacion[catalog["dropoff_datetime"]]>cantidad_finalizacion[repetido]:
                repetido=catalog["dropoff_datetime"]
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


def req_4(catalog,filtro,f1,f2):
    """
    Retorna el resultado del requerimiento 4
    """
    inicio=get_time()
    data={}
    archivo=load_data(data,"nyc-neighborhoods.csv")
    catalog=trans_datos(catalog)
    cantidad=0
    cant_barrios={}
    res={}
    for i in range(0,len(catalog["pikup_datetime"])):
        if catalog["pickup_longitude"][i]!=catalog["dropoff_longitude"][i] or catalog["pickup_latitude"][i]!=catalog["dropoff_latitude"][i]:
            dic={"inicio":catalog["pickup_longitude"][i],"inicio2":catalog["pickup_latitude"][i],"final":catalog["dropoff_longitude"][i],"final2":catalog["dropoff_latitude"][i]}
            if catalog["pikup_datetime"][i]>=datetime.strptime(f1, "%Y-%m-%d %H:%M:%S") and catalog["pikup_datetime"][i]<=datetime.strptime(f2, "%Y-%m-%d %H:%M:%S"):
                cant_barrios[dic]={"cantidad":cant_barrios.get(dic["cantidad"],0)+1, "distancia":cant_barrios.get(dic["distancia"],0)+catalog["trip_distance"][i],\
                    "tiempo":cant_barrios.get(dic["tiempo"],0)+(catalog["dropoff_datetime"][i]-catalog["pickup_datetime"][i]),"costo":cant_barrios.get(dic["cantidad"],0)+catalog["total_amount"][i]\
                        ,"promedio":cant_barrios[mayor]["costo"]/cant_barrios[mayor]["cantidad"]}
                    
                if cantidad==0:
                    mayor=dic
                    menor=dic
                elif cant_barrios[dic]["promedio"]>cant_barrios[mayor]:
                    mayor=dic
                elif cant_barrios[dic]["promedio"]<cant_barrios[menor]:
                    menor=dic
    for i in range(0,len(0,archivo["latitude"])):
        if filtro=="MAYOR":
            if mayor["inicio2"]==archivo["latitude"][i] and mayor["inicio"]==archivo["longitude"][i]:
                res["barrio_inicial"]=archivo["neighborhood"][i]
            if mayor["final2"]==archivo["latitude"][i] and mayor["final"]==archivo["longitude"][i]:
                res["barrio_final"]=archivo["neighborhood"][i]
            res={"promedio_distancia":(cant_barrios[mayor]["distancia"]/cant_barrios[mayor]["cantidad"]),"cantidad":cant_barrios[mayor]["cantidad"],"tiempo_promedio":(cant_barrios[mayor]["tiempo"]/cant_barrios[mayor]["cantidad"]),"promedio_costo":cant_barrios[mayor]["promedio"]}
        elif filtro=="MENOR":
            if menor["inicio2"]==archivo["latitude"][i] and menor["inicio"]==archivo["longitude"][i]:
                res["barrio_inicial"]=archivo["neighborhood"][i]
            if menor["final2"]==archivo["latitude"][i] and menor["final"]==archivo["longitude"][i]:
                res["barrio_final"]=archivo["neighborhood"][i]
            res={"promedio_distancia":(cant_barrios[menor]["distancia"]/cant_barrios[menor]["cantidad"]),"cantidad":cant_barrios[menor]["cantidad"],"tiempo_promedio":(cant_barrios[menor]["tiempo"]/cant_barrios[menor]["cantidad"]),"promedio_costo":cant_barrios[menor]["promedio"]}
    final=get_time()
    tiempo=delta_time(inicio,final)
    res["tiempo_funcion"]=tiempo
    return res
            
            


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
