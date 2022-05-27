import csv
import numpy as np
from ClaseEquipo import Equipo

class ManejaEquipo:
    
    __cantidad = 0
    __dimension = 0
    __incremento = 10
    
    def __init__(self,dimension,incremento=5):
        self.__equipos = np.empty(dimension, dtype=Equipo)
        self.__cantidad = 0
        self.__dimension = dimension
    
    def agregarEquipo(self, unEquipo):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__equipos.resize(self.__dimension)
        self.__equipos[self.__cantidad] = unEquipo
        self.__cantidad += 1
    
    def testArchivo(self):
        archivo = open('Equipos.csv')
        reader = csv.reader(archivo,delimiter=',')
        bandera = True
        n = next(reader)
        cant = int(n[0])
        c = 0
        fila = next(reader)
        while bandera and c < cant:
            ide = int(fila[0])
            nom = fila[1]
            ciudad = fila[2]
            c += 1
            equipo = Equipo(ide, nom, ciudad)
            self.agregarEquipo(equipo)
            try:
                filaS = next(reader)
            except StopIteration:
                bandera = False
            fila = filaS
        archivo.close()
        
    def buscarEquipo(self, ide):
        pos = 0
        bandera = False
        while pos < self.__cantidad and bandera == False:
            if self.__equipos[pos].getID() == ide:
                bandera = True
                return pos
            else:
                pos += 1
    
    def getEquipo(self, pos):
        return self.__equipos[pos]