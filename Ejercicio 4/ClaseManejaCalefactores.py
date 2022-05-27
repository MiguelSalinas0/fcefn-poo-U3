import numpy as np
import csv
from ClaseCalefactorElectrico import Electrico
from ClaseCalefactorGas import Gas
from ClaseCalefactor import Calefactor

class ManejaCalefactores:
    
    __cantidad = 0
    __dimension = 0
    __incremento = 10
    
    def __init__(self,dimension,incremento=5):
        self.__calefactores = np.empty(dimension, dtype=Calefactor)
        self.__cantidad = 0
        self.__dimension = dimension
    
    def agregarCalefactor(self, unCalefactor):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__calefactores.resize(self.__dimension)
        self.__calefactores[self.__cantidad] = unCalefactor
        self.__cantidad += 1
    
    def testArchivoCG(self):
        archivo = open('calefactor-a-gas.csv')
        reader = csv.reader(archivo,delimiter=',')
        bandera = True
        for fila in reader:
            if bandera:
                ''' Saltear Cabecera'''
                bandera = not bandera
            else:
                marca = fila[0]
                modelo = fila[1]
                matricula = fila[2]
                calorias = int(fila[3])
                calefactor = Gas(marca, modelo, matricula, calorias)
                self.agregarCalefactor(calefactor)
        archivo.close()
        
    def testArchivoCE(self):
        archivo = open('calefactor-electrico.csv')
        reader = csv.reader(archivo,delimiter=',')
        bandera = True
        for fila in reader:
            if bandera:
                ''' Saltear Cabecera'''
                bandera = not bandera
            else:
                marca = fila[0]
                modelo = fila[1]
                potencia = int(fila[2])
                calefactor = Electrico(marca, modelo, potencia)
                self.agregarCalefactor(calefactor)
        archivo.close()
    
    def calcCostGas(self):
        cant = int(input('Ingrese la cantidad que se estima consumir de M3: '))
        precio = int(input('Ingrese el precio de M3: '))
        for i in range(self.__cantidad):
            if(type(self.__calefactores[i]) == Gas):
                self.__calefactores[i].calcularConsumo(precio,cant)
    
    def mostGasMenorConsumo(self):
        menor = 9999999999
        j = 0
        for i in range(self.__cantidad):
            if(type(self.__calefactores[i]) == Gas):
                if(self.__calefactores[i].getConsumo() < menor):
                    menor = self.__calefactores[i].getConsumo()
                    j = i
        print('\nCalefactor a gas de menor consumo\n')
        self.mostrar(j)
        
    def calcCostElectrico(self):
        cant = int(input('Ingrese cantidad que se estima consumir de kilowatt/h: '))
        costo = int(input('Ingrese el costo de kilowatt/h: '))
        for i in range(self.__cantidad):
            if(type(self.__calefactores[i]) == Electrico):
                self.__calefactores[i].calcularConsumo(costo,cant)
    
    def mostElectricoMenorConsumo(self):
        menor = 9999999999
        j = 0
        for i in range(self.__cantidad):
            if(type(self.__calefactores[i]) == Electrico):
                if(self.__calefactores[i].getConsumo() < menor):
                    menor = self.__calefactores[i].getConsumo()
                    j = i
        print('\nCalefactor eléctrico de menor consumo\n')
        self.mostrar(j)
    
    def calefactorMenorConsumo(self):
        menor = 999999999
        j = 0
        for i in range(self.__cantidad):
            if(self.__calefactores[i].getConsumo() < menor):
                menor = self.__calefactores[i].getConsumo()
                j = i
        print('\nCalefacor de menor consumo\n')
        if(type(self.__calefactores[j] == Gas)):
           print('Tipo de calefactor: A gas')
        else:
           print('Tipo de calefactor: Eléctrico')
        self.mostrar(j)
    
    def mostrar(self,j):
        print('Marca: {}, modelo: {}'.format(self.__calefactores[j].getMarca(), self.__calefactores[j].getModelo()))