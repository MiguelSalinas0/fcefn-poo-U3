from datetime import datetime
from ClaseContrato import Contrato

class Menu:
    __switcher = None

    def __init__(self):
        self.__switcher = {'1': self.opcion1,
                           '2': self.opcion2,
                           '3':self.opcion3,
                           '4': self.opcion4,
                           '5': self.opcion5,
                           '6': self.salir
                           }

    def opcion(self, op, manejaJugador, manejaEquipo, manejaContrato):
        func = self.__switcher.get(op, lambda: print('Opción no válida'))
        if(op == '1' or op == '2' or op == '3' or op == '4' or op == '5'):
            func(manejaJugador, manejaEquipo, manejaContrato)
        else:
            func()

    def opcion1(self, manejaJugador, manejaEquipo, manejaContrato):
        eq = int(input('Ingrese ID de equipo: '))
        pos = manejaEquipo.buscarEquipo(eq)
        if(pos != None):
            jug = input('Ingrese DNI del jugador: ')
            posJ = manejaJugador.buscarJugador(jug)
            if(posJ != None):
                equipo = manejaEquipo.getEquipo(pos)
                jugador = manejaJugador.getJugador(posJ)
                fechaInicio = input('Ingrese fecha de inicio del contrato ej d/m/Y: ')
                fI = datetime.strptime(fechaInicio, '%d/%m/%Y')
                fechaFin = input('Ingrese fecha de fin del contrato ej d/m/Y: ')
                Ff = datetime.strptime(fechaFin, '%d/%m/%Y')
                monto = float(input('Ingrese pago mensual: '))
                contrato = Contrato(fI, Ff, monto, jugador, equipo)
                manejaContrato.agregarContrato(contrato)
                equipo.agregarContrato(contrato)
                jugador.agregarContrato(contrato)
            else:
                print('\nNo se encontró al jugador')
        else:
            print('\nNo se encontró al equipo')
        
    def opcion2(self, manejaJugador, manejaEquipo, manejaContrato):
        dni = input('Ingrese DNI a buscar: ')
        manejaContrato.buscarDNIcontratos(dni)

    def opcion3(self, manejaJugador, manejaEquipo, manejaContrato):
        ide = int(input('Ingrese ID de equipo: '))
        manejaContrato.contratosVencen6M(ide)
        
    def opcion4(self, manejaJugador, manejaEquipo, manejaContrato):
        equipo = input('Ingrese nombre del equipo a buscar: ')
        manejaContrato.totalContratos(equipo)

    def opcion5(self, manejaJugador, manejaEquipo, manejaContrato):
        manejaContrato.generarArchivo()

    def salir(self):
        print('Saliendo...')
