import numpy as np
import csv
from ClaseFlor import Flor

class ManejaFlor:
    
    __cantidad = 0
    __dimension = 0
    __incremento = 10
    
    def __init__(self,dimension,incremento=5):
        self.__flores = np.empty(dimension, dtype=Flor)
        self.__cantidad = 0
        self.__dimension = dimension
    
    def agregarFlor(self, unaFlor):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__flores.resize(self.__dimension)
        self.__flores[self.__cantidad] = unaFlor
        self.__cantidad += 1
    
    def testArchivo(self):
        archivo = open('Flores.csv')
        reader = csv.reader(archivo,delimiter=',')
        bandera = True
        for fila in reader:
            if bandera:
                ''' Saltear Cabecera'''
                bandera = not bandera
            else:
                num = int(fila[0])
                nom = fila[1]
                color = fila[2]
                descripcion = fila[3]
                flor = Flor(num, nom, color, descripcion)
                self.agregarFlor(flor)
        archivo.close()
    
    def getFlor(self, pos):
        return self.__flores[pos]
                
    def buscarFlorPOS(self, cod):
        pos = 0
        bandera = False
        while pos < len(self.__flores) and bandera == False:
            if self.__flores[pos].getNumero() == cod:
                bandera = True
                return pos
            else:
                pos += 1
                
    def setCantVend(self, pos, cant):
        self.__flores[pos].setCant(cant)
        
    def ordenarLista(self):
        lenght = self.__cantidad - 1
        for i in range(0,lenght):
            for j in range(0,lenght):
                if self.__flores[j] > self.__flores[j+1]:
                    aux = self.__flores[j]
                    self.__flores[j] = self.__flores[j+1]
                    self.__flores[j+1] = aux
    
    def mostrar(self):
        print('\nFlores más vendidas')
        print('Nombre \t\t Color \t\t Cantidad')
        for i in range(5):
            print('{:<10} {:^10} {:^15}'.format(self.__flores[i].getNombre(), self.__flores[i].getColor(), self.__flores[i].getCant()))