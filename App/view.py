from gettext import Catalog
import sys
import logic
import datetime

def new_logic():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función de la lógica donde se crean las estructuras de datos
    new_logic()
    

    

def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    
    print("0- Salir")

def load_data(catalog):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    filename=input("nombre del archivo:")
    return load_data(catalog, filename)




def print_req_1(catalog):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    pasajeros=int(input("numero de pasajeros:"))
    print(logic.req_1(catalog, pasajeros))

    


def print_req_2(catalog):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    medio=input("medio de pago:")
    print=logic.req_2(catalog,medio)
    


def print_req_3(catalog):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    valor_min=float(input("valor minimo:"))
    valor_max=float(input("valor maximo;"))
    # TODO: Imprimir el resultado del requerimiento 3
    print(logic.req_3(catalog, valor_min, valor_max))
    pass


def print_req_4(catalog):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    filtro=input("Ingresa un filtro, tiene que ser MAXIMO O MINIMO")
    f1=input("ingresa la fecha inicio en formato YYYY/MM/DD")
    f2=input("ingresa la fecha final en formato YYYY/MM/DD")
    datetime.date(f1)
    datetime.date(f2)
    print(logic.req_4(catalog,filtro,f1,f2))


def print_req_5(catalog):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    filtro=input("Ingresa un filtro, tiene que ser MAXIMO O MINIMO")
    f1=input("ingresa la fecha inicio en formato YYYY/MM/DD")
    f2=input("ingresa la fecha final en formato YYYY/MM/DD")
    datetime.date(f1)
    datetime.date(f2)
    print(logic.req_5(Catalog, filtro, f1, f2))
    


def print_req_6(catalog):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    barrio_inicio=input("ingresa la barrio de inicio")
    fecha_ini=input("ingresa la fecha inicio en formato YYYY/MM/DD")
    fecha_fin=input("ingresa la fecha final en formato YYYY/MM/DD")
    print(logic.req_6(catalog,barrio_inicio, fecha_ini, fecha_fin))


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
            control = load_data(control)
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
            
        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
