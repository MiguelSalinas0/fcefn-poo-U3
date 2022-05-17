from ClaseRamo import Ramo

class ManejaRamos:
    
    __listaRamos = []
    
    def __init__(self):
        self.__listaRamos = []
        
    def agregarRamo(self, ramo):
        if(type(ramo) == Ramo):
            self.__listaRamos.append(ramo)
    
    