from ClaseLista import ListaPersonal
from ObjectEncoder import ObjectEncoder
from ClaseMenu import Menu

if __name__ == '__main__':
    
    menu = Menu()
    
    jsonF = ObjectEncoder()
    lista = ListaPersonal()
    
    d = jsonF.leerJSONArchivo('personal.json')
    lista = jsonF.decodificarDiccionario(d)
    
    salir = False
    while not salir:
        print('\n_________________________ Menu _________________________\n')
        print('[1]   Insertar personal')
        print('[2]   Agregar personal')
        print('[3]   Mostrar posición')
        print('[4]   Listar datos de docentes investigador por carrera')
        print('[5]   Contar docentes investigadores e investigadores')
        print('[6]   Mostrar listado ordenado por apellido')
        print('[7]   Listar docentes investigadores')
        print('[8]   Consultar gasto de sueldos')
        print('[9]   Modificar sueldo Basico')
        print('[10]  Modificar Porcentaje por cargo')
        print('[11]  Modificar Porcentaje por categoria')
        print('[12]  Modifica Importe Extra')

        print('[13]   Guardar')
        print('[14]   Salir')
        print()
        op = input('Seleccione una opción: ')
        menu.opcion(op,lista,jsonF)
        salir = op == '9'