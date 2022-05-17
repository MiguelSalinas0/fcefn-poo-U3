from ClaseRamo import Ramo

class Menu:
    __switcher = None
    def __init__(self):
        self.__switcher = {'1':self.opcion1,
                           '2':self.opcion2,
                           '3':self.salir
                           }
    def opcion(self,op,manejaR,manejaF):
        func = self.__switcher.get(op, lambda: print('Opción no válida'))
        if(op=='1' or op=='2'):
            func(manejaR,manejaF)
        else:
            func()
    def opcion1(self,manejaR,manejaF):
        bandera = False
        ramo = Ramo()
        while bandera == False:
            cod = input('\nIngrese un código de flor <fin para finalizar> : ')
            if cod == 'fin':
                bandera = True
            else:
                codF = int(cod)
                pos = manejaF.buscarFlorPOS(codF)
                flor = manejaF.buscarFlor(codF)
                cant = int(input('Ingrese la cantidad: '))
                ramo.agregarFlor(flor, cant)
                manejaF.setCantVend(pos,cant)
        manejaR.agregarRamo(ramo)
    def opcion2(self,manejaR,manejaF):
        manejaF.ordenarLista()
        manejaF.mostrar()
    def salir(self):
        print('Saliendo...')