#from ClaseInterface import Interface
#from zope.interface import implementer
from ClaseNodo import Nodo
from ClaseHeladera import Heladera
from ClaseTelevisor import Televisor
from ClaseLavarropa import Lavarropa

#@implementer(Interface)
class ManejaAparatos:
    
    __comienzo = None
    __actual = None
    __indice = 0
    __tope = 0
    
    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato = self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato
    
    def insertarAparato(self, aparato, pos):
        n = Nodo(aparato)
        resultado = False
        if self.__comienzo == None:
            self.__comienzo = n
            resultado = True
            self.__tope += 1
        if pos == 0:
            n.setSiguiente(self.__comienzo)
            self.__comienzo = n
            resultado = True
            self.__tope += 1
        else:
            i = 1
            aux = self.__comienzo
            while aux.getSiguiente() != None and i < pos:
                aux = aux.getSiguiente()
                i += 1
                if i == pos:
                    n.setSiguiente(aux.getSiguiente())
                    aux.setSiguiente(n)
                    resultado = True
                    self.__tope += 1
        return resultado
    
    def agregarAparato(self, aparato):
        nodo = Nodo(aparato)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1
    
    def cuentaMarca(self):
        cant = 0
        for aparato in self.__iter__():
            if(aparato.getMarca().lower() == 'phillips'):
                cant += 1
        return cant
    
    def mostrarPrecioVenta(self):
        print('\nMarca \t\t País de fabricación \t\t Importe de venta')
        for aparato in self.__iter__():
            aparato.calcPrecioVenta()
            print('{:<10} {:>15} {:>25}'.format(aparato.getMarca(),aparato.getPais(),aparato.getPrecioVenta()))
    
    def cantCargSup(self):
        print('\nMarca de lavarropas con carga superior:')
        for aparato in self.__iter__():
            if(type(aparato) == Lavarropa):
                if(aparato.getCarga().lower() == 'superior'):
                    print('Marca: {}'.format(aparato.getMarca()))
    
    def mostrarPos(self,pos):
        for aparato in self.__iter__():
            if(self.__indice == pos):
                if(type(aparato) == Heladera):
                    print('\nEn la posición se encuentra una heladera\n')
                if(type(aparato) == Televisor):
                    print('\nEn la posición se encuentra un televisor\n')
                if(type(aparato) == Lavarropa):
                    print('\nEn la posición se encuentra un lavarropas\n')
    
    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            aparatos = [aparato.toJSON() for aparato in self.__iter__()]
            )
        return d