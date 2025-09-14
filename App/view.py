import sys
import App.logic as logic
from tabulate import tabulate
import csv

csv.field_size_limit(2147483647)

default_limit = 1000
sys.setrecursionlimit(default_limit*10)

def new_logic():
    """
        Se crea una instancia del controlador
    """
    control = logic.new_logic()
    return control

def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8 (Bono)")
    print("0- Salir")

def load_data(control):
    """
    Carga los datos
    """
    filename = 'movies-large.csv'
    control_data = logic.load_data(control, filename)
    return control_data

def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    data = logic.get_data(control, id)
    
    if data:
        headers = ["Campo", "Valor"]
        rows = [
            ["ID", data['id']],
            ["Título", data['title']],
            ["Idioma original", data['original_language']],
            ["Fecha de publicación", data['release_date']],
            ["Duración", str(data['runtime']) + " minutos"],
            ["Presupuesto", str(data['budget'])],
            ["Ingresos", str(data['revenue'])],
            ["Ganancias", "Indefinido" if data['budget'] == 'Indefinido' or data['revenue'] == 'Indefinido' else str(int(data['revenue']) - int(data['budget']))],
            ["Géneros", ', '.join(data['genres'])],
            ["Compañías de producción", ', '.join(data['production_companies'])]
        ]

        print(tabulate(rows, headers=headers, tablefmt='grid'))
    else:
        print("ID no encontrado.")
    

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    
    title = input("Ingrese el nombre de la pelicula: ")
    original_language = input("Ingrese el idioma original: ")
    
    resultado = logic.req_1(control, title, original_language)
    
    if resultado == 0:
        print("No se encontraron películas que cumplan con los criterios.")
    else:
        table_data = [
            ['Título original', resultado['title']],
            ['Idioma original', resultado['original_language']],
            ['Duración (min)', resultado['runtime']],
            ['Fecha de publicación', resultado['release_date']],
            ['Presupuesto', resultado['budget']],
            ['Recaudación', resultado['revenue']],
            ['Ganancia', resultado.get('gains', 'Indefinido')],
            ['Puntaje de calificación', resultado['vote_average']],
        ]
        print("\nDetalles de la película encontrada:")
        print(tabulate(table_data, headers=['Campo', 'Valor'], tablefmt='grid'))


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    pass

def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    status = input("Ingrese el estado de producción de la película (ej.: 'Released', 'Rumored', etc.): ")
    fecha_i = input("Ingrese la fecha inicial (formato YYYY-MM-DD): ")
    fecha_f = input("Ingrese la fecha final (formato YYYY-MM-DD): ")

    resultado = logic.req_4(control, status, fecha_i, fecha_f)
    
    if resultado[0] == 0 or resultado == None:
        print("No se encontraron películas que cumplan con los criterios.")
    else:
        print("Número total de películas que cumplen con el criterio: " + str(resultado[0]))
        print("Tiempo promedio de duración de las películas: " + str(resultado[1]) + " minutos")
        print("\nDetalles de las primeras películas encontradas (hasta 10):")
        
        table_data = []
        for movie in resultado[2]['elements']:
            table_data.append([
                movie['release_date'],
                movie['title'],
                movie['budget'],
                movie['revenue'],
                str(movie.get('gains', 'Indefinido')),
                movie['runtime'],
                movie['vote_average'],
                movie['original_language']
            ])

        headers = ['Fecha de publicación', 'Título original', 'Presupuesto', 'Recaudación', 'Ganancia', 'Duración (min)', 'Puntaje de calificación', 'Idioma original']
        print(tabulate(table_data, headers=headers, tablefmt='grid'))


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
