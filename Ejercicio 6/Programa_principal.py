from ClaseMenu import Menu
from ClaseManejaAparatos import ManejaAparatos
from ObjectEncoder import ObjectEncoder

if __name__ == '__main__':
    
    jsonF = ObjectEncoder()
    lista = ManejaAparatos()
    
    diccionario = jsonF.leerJSONArchivo('aparatoselectronicos.json')
    
    lista = jsonF.decodificarDiccionario(diccionario)
    
    menu = Menu()
    
    salir = False
    while not salir:
        print('\n_______________________ Menu _______________________\n')
        print('[1]   Insertar un aparato')
        print('[2]   Agregar un aparato')
        print('[3]   Ingresar posición en listado')
        print('[4]   Cantidad de aparatos cuya marca es Phillips')
        print('[5]   Marca de lavarropas con carga superior')
        print('[6]   Mostrar todos los aparatos a la venta')
        print('[7]   Guardar en archivo JSON')
        print('[8]   Salir')
        print()
        op = input('Seleccione una opcion: ')
        menu.opcion(op, lista, jsonF)
        salir = op == '8'
    