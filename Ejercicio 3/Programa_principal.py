from ClaseManejaJugador import ManejaJugador
from ClaseManejaEquipo import ManejaEquipo
from ClaseManejaContrato import ManejaContrato
from ClaseMenu import Menu

if __name__ == '__main__':

    menu = Menu()

    manejaContrato = ManejaContrato(5)

    manejaJugador = ManejaJugador()
    manejaJugador.testArchivo()

    manejaEquipo = ManejaEquipo(5)
    manejaEquipo.testArchivo()

    salir = False
    while not salir:
        print('\n______________ Menu ______________\n')
        print('[1]   Crear un nuevo contrato')
        print('[2]   Consultar jugadores contratados')
        print('[3]   Consultar contratos')
        print('[4]   Obtener importe de contratos')
        print('[5]   Guardar contratos')
        print('[6]   Salir')
        print()
        op = input('Seleccione una opcion: ')
        menu.opcion(op, manejaJugador, manejaEquipo, manejaContrato)
        salir = op == '6'
