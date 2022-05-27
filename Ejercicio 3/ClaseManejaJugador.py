import csv
from ClaseJugador import Jugador

class ManejaJugador:
    
    __listado = []
    
    def __init__(self):
        self.__listado = []
    
    def agregarJugador(self, jugador):
        if(type(jugador) == Jugador):
            self.__listado.append(jugador)
    
    def testArchivo(self):
        archivo = open('Jugadores.csv')
        reader = csv.reader(archivo,delimiter=',')
        bandera = True
        for fila in reader:
            if bandera:
                ''' Saltear Cabecera'''
                bandera = not bandera
            else:
                nombre = fila[0]
                dni = fila[1]
                ciudad = fila[2]
                pais = fila[3]
                fechaN = fila[4]
                jugador = Jugador(nombre, dni, ciudad, pais, fechaN)
                self.agregarJugador(jugador)
        archivo.close()
    
    def buscarJugador(self, dni):
        pos = 0
        bandera = False
        while pos < len(self.__listado) and bandera == False:
            if self.__listado[pos].getDNI() == dni:
                bandera = True
                return pos
            else:
                pos += 1
    
    def getJugador(self, pos):
        return self.__listado[pos]
    