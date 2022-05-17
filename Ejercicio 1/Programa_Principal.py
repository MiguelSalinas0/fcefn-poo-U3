from ClaseManejaFacultades import ManejaFacultades
from ClaseMenu import Menu

if __name__ == "__main__":
    
    menu = Menu()
    manejaFA = ManejaFacultades()
    manejaFA.testArchivo()
    
    salir = False
    while not salir:
        print('\n__________________ Menu __________________\n')
        print('[1]   Listar carreras de una universidad')
        print('[2]   Mostrar datos de una carrera')
        print('[3]   Salir')
        print()
        op = input('Seleccione una opción: ')
        menu.opcion(op, manejaFA)
        salir = op == '3'
        