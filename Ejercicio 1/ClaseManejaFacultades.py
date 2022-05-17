import csv
from ClaseFacultad import Facultad

class ManejaFacultades:
    
    __listaFacultades = []
    
    def __init__(self):
        self.__listaFacultades = []
    
    def testArchivo(self):
        archivo = open('Facultades.csv')
        reader = csv.reader(archivo,delimiter=',')
        
        fila=next(reader)
        bandera = True
        
        while bandera:
            cod = int(fila[0])
            nom = fila[1]
            direccion = fila[2]
            localidad = fila[3]
            tel = fila[4]
            listaCarrera = []
            filaCarrera=next(reader)
            while bandera and (int(fila[0])==int(filaCarrera[0])):
                listaCarrera.append(filaCarrera)
                try:
                    filaCarrera=next(reader)
                except StopIteration:
                    bandera=False
            fila=filaCarrera
            nuevaFacultad = Facultad(cod,nom,direccion,localidad,tel,listaCarrera)
            self.__listaFacultades.append(nuevaFacultad)
            
    def buscarFacultad(self, nro):
        pos = 0
        bandera = False
        while pos < len(self.__listaFacultades) and bandera == False:
            if self.__listaFacultades[pos].getCodigo() == nro:
                bandera = True
                return pos
            else:
                pos += 1
    
    def mostrar(self, pos):
        self.__listaFacultades[pos].mostrarFacultad()
        
    def buscarCarrera(self, carrera):
        pos = 0
        bandera = False
        while pos < len(self.__listaFacultades) and bandera == False:
            algo = self.__listaFacultades[pos].getCarrera(carrera)
            if (algo == True):
                bandera = True
            else:
                pos += 1
                
        if pos == len(self.__listaFacultades):
            print('\nNo se encontró la carrera')
            