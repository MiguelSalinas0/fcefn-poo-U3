from ClaseNodo import Nodo
from ClaseDocente import Docente
from zope.interface import implementer
from ClaseDocenteInvestigador import DocenteInvestigador
from ClaseInvestigador import Investigador
from ejer5 import Coleccion
from InterfazT import ITesorero
from interfazD import IDirector
@implementer(Coleccion)
@implementer(ITesorero)
@implementer(IDirector)
class ListaPersonal:
    
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
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
            return dato
    
    def agregarPersonal(self, personal):
        nodo = Nodo(personal)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1
    
    def insertar(self,agente,pos):
        n = Nodo(agente)
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
    
    def mostrarPos(self,pos):
        for item in self.__iter__():
            if(self.__indice == pos):
                if(type(item) == DocenteInvestigador):
                    print('\nEn la posición se encuentra un docente investigador\n')
                if(type(item) == Investigador):
                    print('\nEn la posición se encuentra un investigador\n')
                if(type(item) == Docente):
                    print('\nEn la posición se encuentra un docente\n')
    
    def contarDyDI(self,area):
        totalI = 0
        totalDI = 0
        for item in self.__iter__():
            if(type(item) == DocenteInvestigador):
                if(item.getArea().lower() == area.lower()):
                    totalDI += 1
            if(type(item) == Investigador):
                if(item.getArea().lower() == area.lower()):
                    totalI += 1
        print('\nTotal de investigadores: {}'.format(totalI))
        print('Total de docentes investigadores: {}'.format(totalDI))
    
    def listarDI(self, cat):
        total = 0.0
        for item in self.__iter__():
            if(type(item) == DocenteInvestigador):
                if(item.getCategoriaInv().lower() == cat.lower()):
                    print('\nApellido y nombre: {}, {}'.format(item.getApellido(), item.getNombre()))
                    print('Importe extra: {}'.format(item.getExtra()))
                    total += item.getExtra()
        print('\nImporte total que se debe solicitar en concepto de importe extra: {} '.format(total))
    
    def ordenarPorApellido(self):
        try:
            k = cota = p = None
            aux = None
            
            while(k != self.__comienzo):
                k = self.__comienzo
                p = self.__comienzo
                while(p.getSiguiente()!=cota):
                    if(p.getDato().getApellido().lower() > p.getSiguiente().getDato().getApellido().lower()):
                        aux = p.getSiguiente().getDato()
                        p.getSiguiente().setDato(p.getDato())
                        p.setDato(aux)
                        k=p
                    p=p.getSiguiente()
                cota = k.getSiguiente()
        except IndexError:
            print('Fuera de rango')
    
    def mostrar6(self):
        for item in self.__iter__():
            item.calcularSueldo()
            print('\nApellido y nombre: {}, {}'.format(item.getApellido(),item.getNombre()))
            if(type(item) == Docente):
                print('Agente: Docente')
            if(type(item) == DocenteInvestigador):
                print('Agente: Docente Investigador')
            if(type(item) == Investigador):
                print('Agente: Investigador')
            print('Sueldo: {}'.format(item.getSueldo()))
    
    def ordenarPorNombre(self):
        try:
            k = cota = p = None
            aux = None
            
            while(k != self.__comienzo):
                k = self.__comienzo
                p = self.__comienzo
                while(p.getSiguiente()!=cota):
                    if(p.getDato().getNombre().lower() > p.getSiguiente().getDato().getNombre().lower()):
                        aux = p.getSiguiente().getDato()
                        p.getSiguiente().setDato(p.getDato())
                        p.setDato(aux)
                        k=p
                    p=p.getSiguiente()
                cota = k.getSiguiente()
        except IndexError:
            print('Fuera de rango')
    
    def mostrar4(self,carrera):
        for item in self.__iter__():
            if(type(item) == DocenteInvestigador):
                if(item.getCarrera().lower() == carrera.lower()):
                    print('\nApellido y nombre: {}, {}'.format(item.getApellido(),item.getNombre()))
    
    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            personal = [personal.toJSON() for personal in self.__iter__()]
            )
        return d
    def ModificarBasico(self,dni,nuevoBasico):
        for item in self.__iter__():
            if dni==item.getCuil():
                basico=float(input('Ingresar nuevo sueldo Basico:'))
                item.setBasico(basico)
    def modificarPorcentajeporcargo(self,dni,nuevoPorcentaje):
        for item in self.__iter__():
            if dni==item.getCuil():
                
                item.setVariale(nuevoPorcentaje)
    def modificarPorcentajeporcategoria(self,dn,nuevoPorcentaje):
        for item in self.__iter__():
            if dn==item.getCuil():
                
                item.setVariale(nuevoPorcentaje)
    def modificaImporteExtra(self,dni,nuevoImporteExtra):
        for item in self.__iter__():
            if dni==item.getCuil():
                i=float(input('Ingresar nuevo importe extra:'))
                item.setExtra(i)
    def gastosSueldoPorEmpleado(self,dni):
        for item in self.__iter__():
            if dni==item.getCuil():
                print('Sueldo {}'.format(item.getSueldo()))
                