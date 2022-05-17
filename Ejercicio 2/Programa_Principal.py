from ClaseManejaFlores import ManejaFlor
from ClaseManejaRamos import ManejaRamos
from ClaseMenu import Menu

if __name__ == '__main__':
    
    menu = Menu()
    
    manejaF = ManejaFlor(10)
    manejaF.testArchivo()
    
    manejaR = ManejaRamos()
    
    salir = False
    while not salir:
        print('\n________________ Menu ________________\n')
        print('[1]   Registrar un ramo vendido')
        print('[2]   Listar las 5 flores más vendidas')
        print('[3]   Salir')
        print()
        op = input('Seleccione una opcion: ')
        menu.opcion(op, manejaR, manejaF)
        salir = op == '3'
        