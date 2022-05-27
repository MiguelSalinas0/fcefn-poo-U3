import numpy as np
from ClaseContrato import Contrato

class ManejaContrato:
    
    __cantidad = 0
    __dimension = 0
    __incremento = 10
    
    def __init__(self,dimension,incremento=5):
        self.__contratos = np.empty(dimension, dtype=Contrato)
        self.__cantidad = 0
        self.__dimension = dimension
    
    def agregarContrato(self, unContrato):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__contratos.resize(self.__dimension)
        self.__contratos[self.__cantidad] = unContrato
        self.__cantidad += 1
    
    def mostrar(self):
        for i in range(self.__cantidad):
            print(self.__contratos[i])
    
    def buscarDNIcontratos(self, dni):
        for i in range(self.__cantidad):
            jugador = self.__contratos[i].getJugador()
            dniJ = jugador.getDNI()
            if(dniJ == dni):
                print(self.__contratos[i].getEquipo())
                print('Fecha fin de contrato: {}'.format(self.__contratos[i].getFechaFin()))
        
    def totalContratos(self, NomEquipo):
        total = 0.0
        for i in range(self.__cantidad):
            equipo = self.__contratos[i].getEquipo()
            nombre = equipo.getNombre()
            if(nombre.lower() == NomEquipo.lower()):
                total += self.__contratos[i].getPagoMensual()
        print('\nImporte total a pagar: {}'.format(total))
    
    def contratosVencen6M(self, idE):
        print('\nContratos que vencen en menos de 6 meses\n')
        for i in range(self.__cantidad):
            equipo = self.__contratos[i].getEquipo()
            if(equipo.getID() == idE):
                meses = self.__contratos[i].calcularMeses()
                if(meses < 6):
                    jugador = self.__contratos[i].getJugador()
                    print('Jugador: {}, DNI: {}'.format(jugador.getNombre(), jugador.getDNI()))
    
    def generarArchivo(self):
        archivo = open('Contratos.csv', 'w')
        archivo.write('DNI jugador,Nombre equipo,Fecha inicio,Fecha fin,Pago mensual\n')
        for i in range(self.__cantidad):
            jugador = self.__contratos[i].getJugador()
            dni = jugador.getDNI()
            equipo = self.__contratos[i].getEquipo()
            nom = equipo.getNombre()
            archivo.write('{},{},{},{},{}\n'.format(dni,nom,self.__contratos[i].getFechaInicio(),self.__contratos[i].getFechaFin(),self.__contratos[i].getPagoMensual()))
        archivo.close()