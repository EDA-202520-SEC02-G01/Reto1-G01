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
    catalog["pickup_datetime"] = [datetime.strptime(x, "%Y-%m-%d %H:%M:%S") for x in catalog["pickup_datetime"]]
    catalog["dropoff_datetime"] = [datetime.strptime(x, "%Y-%m-%d %H:%M:%S") for x in catalog["dropoff_datetime"]]
    catalog["passenger_count"] = [int(x) for x in catalog["passenger_count"]]
    catalog["trip_distance"] = [float(x) for x in catalog["trip_distance"]]
    catalog["tip_amount"] = [float(x) for x in catalog["tip_amount"]]
    catalog["tolls_amount"] = [float(x) for x in catalog["tolls_amount"]]
    catalog["total_amount"] = [float(x) for x in catalog["total_amount"]]
    return catalog
    

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
            fecha=datetime.syrptime(catalog["pickup_datetime"][i],"%Y-%m-%d %H:%M:%S")
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
    costo=0
    distancia=0
    pedajes=0
    cantidad_pasajeros={}
    mayor=0
    propina=0
    cantidad_finalizacion={}
    tiempo=0
    for i in range(0,len(catalog["payment_type"])):
        if catalog["payment_type "][i]==medio:
            cantidad+=1
            costo+=catalog["total_amount"][i]
            distancia+=catalog["trip_distance"][i]
            pedajes+=catalog["tolls_amount"][i]
            cantidad_pasajeros[catalog["passenger_count"][i]]=cantidad_pasajeros.get(catalog["passenger_count"][i],0)+1
            cantidad_finalizacion=[catalog["dropoff_datetime"][i].date()]=cantidad_finalizacion.get(catalog["dropoff_datetime"][i],0)+1
            if cantidad==1:
                mayor=catalog["passenger_count"][i]
                repetido=catalog["dropoff_datetime"][i].date()
            elif cantidad_pasajeros[catalog["passenger_count"][i]]>cantidad_pasajeros[mayor]:
                mayor=catalog["passenger_count"][i]
            elif cantidad_finalizacion[catalog["dropoff_datetime"][i].date()]>cantidad_finalizacion[repetido]:
                repetido=catalog["dropoff_datetime"][i].date()
            propina+=catalog["tip_amount"][i]
            tiempo+=(catalog["dropoff_datetime"][i]-catalog["pickup_datetime"][i])
    tiempo=tiempo/60
    dic={"num_trayectos":cantidad,
         "tiempo_promedio":tiempo/cantidad,
         "costo_promedio":costo/cantidad,
         "pasajeros_frec":str(mayor)+" - "+str(cantidad_pasajeros[mayor]),
         "propina_promedio":propina/cantidad,
         "fecha_mas trayectos":repetido}
    final=get_time()
    tiempo=delta_time(final,inicio)
    dic["Tiempo"]=tiempo
    return dic
    
    
def req_3(catalog, valor_min, valor_max):
    """
    Retorna el resultado del requerimiento 3
    """
    inicio = get_time()
    catalog = trans_datos(catalog)
    total_trayectos = 0
    tiempo_promedio = 0
    costo_promedio = 0
    distancia_promedio = 0
    peajes_promedio = 0
    propina_promedio = 0
    pasajeros_frecuentes = {}
    fecha_finalizacion = {}

    for i in range(len(catalog["total_amount"])):
        pago = catalog["total_amount"][i]
        if valor_min <= pago and pago <= valor_max:
            total_trayectos += 1
            duracion = catalog["dropoff_datetime"][i] - catalog["pickup_datetime"][i]
            tiempo_promedio += duracion.total_seconds() / 60
            costo_promedio += pago
            distancia_promedio += catalog["trip_distance"][i]
            peajes_promedio += catalog["tolls_amount"][i]
            propina_promedio += catalog["tip_amount"][i]
            pasajeros = catalog["passenger_count"][i]
            pasajeros_frecuentes[pasajeros] = pasajeros_frecuentes.get(pasajeros, 0) + 1
            fecha = catalog["dropoff_datetime"][i].date()
            fecha_finalizacion[fecha] = fecha_finalizacion.get(fecha, 0) + 1
            
    if total_trayectos == 0:
        dicc = {
            "total_trayectos": 0,
            "tiempo_promedio": 0,
            "costo_promedio": 0,
            "distancia_promedio": 0,
            "peajes_promedio": 0,
            "pasajeros_frecuentes": "N/A",
            "propina_promedio": 0,
            "fecha_finalizacion": "N/A",
            "tiempo_ejecucion": delta_time(inicio, get_time())
        }
    else:
        pasajero_mas_frec = max(pasajeros_frecuentes, key=pasajeros_frecuentes.get)
        fecha_mas_frec = max(fecha_finalizacion, key=fecha_finalizacion.get)
        dicc = {
            "total_trayectos": total_trayectos,
            "tiempo_promedio": tiempo_promedio / total_trayectos,
            "costo_promedio": costo_promedio / total_trayectos,
            "distancia_promedio": distancia_promedio / total_trayectos,
            "peajes_promedio": peajes_promedio / total_trayectos,
            "pasajeros_frecuentes": f"{pasajero_mas_frec} - {pasajeros_frecuentes[pasajero_mas_frec]}",
            "propina_promedio": propina_promedio / total_trayectos,
            "fecha_finalizacion": fecha_mas_frec.strftime("%Y-%m-%d"),
            "tiempo_ejecucion": delta_time(inicio, get_time())
    }
    return dicc


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
    for i in range(0,len(catalog["pickup_datetime"])):
        if catalog["pickup_longitude"][i]!=catalog["dropoff_longitude"][i] or catalog["pickup_latitude"][i]!=catalog["dropoff_latitude"][i]:
            dic=(catalog["pickup_longitude"][i],\
                catalog["pickup_latitude"][i],\
                catalog["dropoff_longitude"][i],\
                catalog["dropoff_latitude"][i])
            if catalog["pikup_datetime"][i].date()>=datetime.strptime(f1, "%Y-%m-%d").date() and catalog["pikup_datetime"][i].date()<=datetime.strptime(f2, "%Y-%m-%d").date():
                if dic not in cant_barrios:
                    cant_barrios[dic]={
                    "cantidad":0, 
                    "distancia":0,
                    "tiempo":0,
                    "costo":0,
                    "promedio":0}
                    
                cant_barrios[dic]["cantidad"]+=1
                cant_barrios[dic]["distancia"]+=catalog["trip_distance"][i]
                cant_barrios[dic]["tiempo"]+=(catalog["dropoff_datetime"][i]-catalog["pickup_datetime"][i])/60
                cant_barrios[dic]["costo"]+=catalog["total_amount"][i]
                cant_barrios[dic]["promedio"]=cant_barrios[dic]["costo"]/cant_barrios[dic]["cantidad"]
               
                if cantidad==0:
                    mayor=dic
                    menor=dic
                elif cant_barrios[dic]["promedio"]>cant_barrios[mayor]:
                    mayor=dic
                elif cant_barrios[dic]["promedio"]<cant_barrios[menor]:
                    menor=dic
                    
    for i in range(0,len(archivo["latitude"])):
        
        if filtro=="MAYOR":
            if mayor[1]==archivo["latitude"][i] and mayor[0]==archivo["longitude"][i]:
                res["barrio_inicial"]=archivo["neighborhood"][i]
            if mayor[3]==archivo["latitude"][i] and mayor[2]==archivo["longitude"][i]:
                res["barrio_final"]=archivo["neighborhood"][i]
            res={"promedio_distancia":(cant_barrios[mayor]["distancia"]/cant_barrios[mayor]["cantidad"]),"cantidad":cant_barrios[mayor]["cantidad"],"tiempo_promedio":(cant_barrios[mayor]["tiempo"]/cant_barrios[mayor]["cantidad"]),"promedio_costo":cant_barrios[mayor]["promedio"]}
        elif filtro=="MENOR":
            if menor[1]==archivo["latitude"][i] and menor[0]==archivo["longitude"][i]:
                res["barrio_inicial"]=archivo["neighborhood"][i]
            if menor[3]==archivo["latitude"][i] and menor[2]==archivo["longitude"][i]:
                res["barrio_final"]=archivo["neighborhood"][i]
            res={"promedio_distancia":(cant_barrios[menor]["distancia"]/cant_barrios[menor]["cantidad"]),"cantidad":cant_barrios[menor]["cantidad"],"tiempo_promedio":(cant_barrios[menor]["tiempo"]/cant_barrios[menor]["cantidad"]),"promedio_costo":cant_barrios[menor]["promedio"]}
   
    final=get_time()
    tiempo=delta_time(inicio,final)
    res["tiempo_funcion"]=tiempo
    return res
            
            


def req_5(catalog, filtro, f1, f2):
    """
    Retorna el resultado del requerimiento 5
    """
    inicio=get_time()
    catalog=trans_datos(catalog)
    res={}
    franjas={}
    for i in range(0, len(catalog["pickup_datetime"])):
        if catalog["pickup_datetime"][i]>=f1 and catalog["pickup_datetime"][i]<=f2:
            hora=catalog["pickup_datetime"][i].hour
            duracion = (catalog["dropoff_datetime"][i] - catalog["pickup_datetime"][i]).total_seconds() / 60
            costo = catalog["total_amount"][i]
            pasajeros = catalog["passenger_count"][i]
            if hora not in franjas:
                franjas[hora]={"conteo":0, "suma_costos":0,"suma_duracion":0, "suma_pasajeros":0, "max_costo":costo, "min_costo":costo}
            franjas[hora]["suma_costos"] += costo
            franjas[hora]["conteo"] += 1
            franjas[hora]["suma_duracion"] += duracion
            franjas[hora]["suma_pasajeros"] += pasajeros
    for hora in franjas:
        franjas[hora]["costo_promedio"]=franjas[hora]["suma_costos"]/franjas[hora]["conteo"]
        franjas[hora]["duracion_promedio"] = franjas[hora]["suma_duracion"] / franjas[hora]["conteo"]
        franjas[hora]["pasajeros_promedio"] = franjas[hora]["suma_pasajeros"] / franjas[hora]["conteo"]
    
    if filtro == "MAYOR":
        filt = min(franjas, key=lambda hora: franjas[hora]["costo_promedio"])
        resf=franjas[filt]
    else:
        filt = max(franjas, key=lambda hora: franjas[hora]["costo_promedio"])
        resf=franjas[filt]
    
    res["filtro"]=filtro
    res["franja_de_horas"]=[filt,filt+1]
    res["max_o_min_franja"]=resf
    res["Tiempo_ejecucion"]=delta_time(inicio,get_time())
    
    
    return res  
    

def req_6(catalog,barrio_inicio, fecha_ini, fecha_fin):
    """
    Retorna el resultado del requerimiento 6
    """    
    inicio = get_time()
    catalog = trans_datos(catalog)
    fecha_ini = datetime.strptime(fecha_ini, "%Y-%m-%d")
    fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d")
    total_trayectos = 0
    distancia_total = 0
    tiempo_total = 0
    destinos = {}
    pagos = {}
    pagos_total = {}
    tiempo_pago = {}

    for i in range(len(catalog["pickup_datetime"])):
        fecha_pickup = catalog["pickup_datetime"][i]
        if fecha_ini <= fecha_pickup.date() <= fecha_fin:
            if catalog["pickup_barrio"][i] == barrio_inicio:
                total_trayectos += 1
                distancia_total += catalog["trip_distance"][i]
                duracion = catalog["dropoff_datetime"][i] - catalog["pickup_datetime"][i]
                tiempo_total += duracion.total_seconds() / 60
                barrio_destino = catalog["dropoff_barrio"][i]
                destinos[barrio_destino] = destinos.get(barrio_destino, 0) + 1
                pago = catalog["payment_type"][i]
                pagos[pago] = pagos.get(pago, 0) + 1
                pagos_total[pago] = pagos_total.get(pago, 0) + catalog["total_amount"][i]
                tiempo_pago[pago] = tiempo_pago.get(pago, 0) + duracion.total_seconds() / 60

    if total_trayectos == 0:
        dicc = {
            "tiempo_ejecucion": delta_time(inicio, get_time()),
            "total_trayectos": 0,
            "distancia_promedio": 0,
            "tiempo_promedio": 0,
            "barrio_destino_mas_visitado": "N/A",
            "medios_pago": []
        }
         
    else:
        barrio_destino_mas_visitado = max(destinos, key=destinos.get)
        medio_mas_usado = max(pagos, key=pagos.get)
        medio_mas_recaudo = max(pagos_total, key=pagos_total.get)

        medios_pago = []
        for pago in pagos:
            medios_pago.append({
                "tipo_pago": pago,
                "cantidad_trayectos": pagos[pago],
                "precio_promedio": pagos_total[pago] / pagos[pago],
                "es_mas_usado": pago == medio_mas_usado,
                "es_mas_recaudo": pago == medio_mas_recaudo,
                "tiempo_promedio": tiempo_pago[pago] / pagos[pago]
            })

        dicc = {
            "tiempo_ejecucion": delta_time(inicio, get_time()),
            "total_trayectos": total_trayectos,
            "distancia_promedio": distancia_total / total_trayectos,
            "tiempo_promedio": tiempo_total / total_trayectos,
            "barrio_destino_mas_visitado": barrio_destino_mas_visitado,
            "medios_pago": medios_pago
        }
        return dicc


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
