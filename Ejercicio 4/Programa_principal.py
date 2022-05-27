from ClaseManejaCalefactores import ManejaCalefactores
from ClaseMenu import Menu

if __name__ == '__main__':
    
    menu = Menu()
    
    dimension = int(input('Ingrese dimensión para el arreglo de calefactores: '))
    
    manejaCalefactor = ManejaCalefactores(dimension)
    
    manejaCalefactor.testArchivoCE()
    manejaCalefactor.testArchivoCG()
    
    salir = False
    while not salir:
        print('\n_________________ Menu _________________\n')
        print('[1]   Calefactor a gas de menor consumo')
        print('[2]   Calefactor eléctrico de menor consumo')
        print('[3]   Mostrar calefactor de menor consumo')
        print('[4]   Salir')
        print()
        op = input('Seleccione una opcion: ')
        menu.opcion(op, manejaCalefactor)
        salir = op == '4'