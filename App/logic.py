import time
import json
import csv
import os
from datetime import datetime
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(root_dir)
from DataStructures.Map import map_linear_probing as mp
from DataStructures.List import array_list as lt

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    catalog = {}
    
    num_elements = 1000  
    load_factor = 0.75    
    prime = 109345121
    
    catalog = mp.new_map(num_elements, load_factor, prime)
    
    return catalog


# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    
    data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/Challenge-2/'
    file_path = os.path.join(data_dir, filename)
   
    with open(file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
    
        for row in csv_reader:
            
            id = row.get('id')
            
            movie_data = {
                'budget': row.get('budget', 'Indefinido'),
                'genres': json.loads(row.get('genres', '[]')),
                'original_language': row.get('original_language', 'Indefinido'),
                'popularity': row.get('popularity', 'Indefinido'),
                'production_companies': json.loads(row.get('production_companies', '[]')),
                'release_date': row.get('release_date', 'Indefinido'),
                'revenue': row.get('revenue', 'Indefinido'),
                'runtime': row.get('runtime', 'Indefinido'),
                'status': row.get('status', 'Indefinido'),
                'title': row.get('title', 'Indefinido'),
                'vote_average': row.get('vote_average', 'Indefinido'),
                'vote_count': row.get('vote_count', 'Indefinido'),
                }
            
            if id:
                mp.put(catalog, id, movie_data)
          
    

                
def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    movie = mp.get(catalog, id)
    
    if movie:
        return movie['value']
    else:
        return None

def req_1(catalog, title, original_language):
    """
    Retorna el resultado del requerimiento 1
    """
    movies = mp.value_set(catalog)
    
    for movie in movies['elements']:
        if movie['title'].lower() == title.lower() and movie['original_language'].lower() == original_language.lower():
            movie['gains'] = int(movie['revenue']) - int(movie['budget']) if movie['revenue'] != 'Indefinido' and movie['revenue'] != 'Indefinido' else 'Indefinido'
            return movie
        
    return None
    
    



def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    pass

def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog, status, fecha_i, fecha_f):
    """
    Retorna el resultado del requerimiento 4
    """
    movies = mp.value_set(catalog)
    numero_peliculas = 0
    duracion_total = 0
    lista_resp = lt.new_list()
    fecha_i_dt = datetime.strptime(fecha_i, "%Y-%m-%d")
    fecha_f_dt = datetime.strptime(fecha_f, "%Y-%m-%d")

    
    for movie in movies['elements']:
        movie_fecha_dt = datetime.strptime(movie['release_date'], "%Y-%m-%d")
        if movie['status'].lower() == status.lower() and fecha_i_dt <= movie_fecha_dt <= fecha_f_dt:
            numero_peliculas += 1
            duracion_total += float(movie['runtime']) if movie['runtime'] != 'Indefinido' else 0
            movie['gains'] = int(movie['revenue']) - int(movie['budget']) if movie['revenue'] != 'Indefinido' and movie['revenue'] != 'Indefinido' else 'Indefinido'
            lt.add_last(lista_resp, movie)
            
    if lt.size(lista_resp) > 1:
        def sort_crit(movie1, movie2):
            date1 = datetime.strptime(movie1['release_date'], "%Y-%m-%d")
            date2 = datetime.strptime(movie2['release_date'], "%Y-%m-%d")
            return date1 > date2

    
    lista_resp = lt.merge_sort(lista_resp, sort_crit)
        
    if numero_peliculas > 0:
        duracion_promedio = float(round(duracion_total / numero_peliculas, 3))
    else:
        duracion_promedio = 0
        
    if lt.size(lista_resp) > 20:
        lista_resp["elements"][:10]
        lista_resp["size"] = 10
        
    return numero_peliculas, duracion_promedio, lista_resp



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


def req_7(catalog, production_company, anio_i, anio_f ):
    """
    Retorna el resultado del requerimiento 7
    """
    movies = mp.value_set(catalog)
    anio_i = int(anio_i)
    anio_f = int(anio_f)
    lista_resp = lt.new_list()
    dicc_anios = {}
    
    for movie in movies["elements"]:
        if movie['release_date'] != 'Indefinido':
            anio = int(movie['release_date'][:4])
            if anio_i <= anio <= anio_f:
                for company in movie['production_companies']:
                    if company['name'].lower() == production_company.lower() and movie['status'] == "Released":
                        
                        if anio not in dicc_anios:
                            dicc_anios[anio] = {
                                "total_peliculas": 0,
                                "votacion_promedio": 0,
                                "duracion_promedio": 0,
                                "ganancias_totales": 0,
                                "mejor_pelicula": {"title": "", "votacion_promedio": 0},
                                "peor_pelicula": {"title": "", "votacion_promedio": 1000000}
                            }
                            
                        dicc_anios[anio]["total_peliculas"] += 1
                        dicc_anios[anio]["votacion_promedio"] += float(movie['vote_average'])
                        dicc_anios[anio]["duracion_promedio"] += float(movie['runtime']) if movie['runtime'] != 'Indefinido' else 0
                        if movie['revenue'] != 'Indefinido' and movie['budget'] != 'Indefinido':
                            dicc_anios[anio]["ganancias_totales"] += int(movie['revenue']) - int(movie['budget'])
                            
                        if float(movie['vote_average']) > dicc_anios[anio]['mejor_pelicula']['votacion_promedio']:
                            dicc_anios[anio]['mejor_pelicula'] = {
                                "title": movie['title'],
                                "votacion_promedio": float(movie['vote_average'])
                            }
                            
                        if float(movie['vote_average']) < dicc_anios[anio]['peor_pelicula']['votacion_promedio']:
                            dicc_anios[anio]['peor_pelicula'] = {
                                "title": movie['title'],
                                "votacion_promedio": float(movie['vote_average'])
                            }
                            
    for anio, diccionario in dicc_anios.items():
        if diccionario['total_peliculas'] > 0:
            diccionario["votacion_promedio"] /= diccionario["total_peliculas"]
            diccionario["duracion_promedio"] /= diccionario["total_peliculas"]
            
        lt.add_last(lista_resp, {
            "anio": anio,
            "total_peliculas": diccionario["total_peliculas"],
            "votacion_promedio": diccionario["votacion_promedio"],
            "duracion_promedio": diccionario["duracion_promedio"],
            "ganancias_totales": diccionario["ganancias_totales"],
            "mejor_pelicula": diccionario["mejor_pelicula"],
            "peor_pelicula": diccionario["peor_pelicula"]
        })
        
    print(movies)
    return lista_resp

        


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
