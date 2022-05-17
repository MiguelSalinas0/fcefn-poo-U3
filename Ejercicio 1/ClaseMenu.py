class Menu:
    __switcher = None
    def __init__(self):
        self.__switcher = {'1':self.opcion1,
                           '2':self.opcion2,
                           '3':self.salir
                           }
    def opcion(self,op,manejaFA):
        func = self.__switcher.get(op, lambda: print('Opción no válida'))
        if(op=='1' or op=='2'):
            func(manejaFA)
        else:
            func()
    def opcion1(self,manejaFA):
        codigo = int(input('\nIngrese código de universidad: '))
        pos = manejaFA.buscarFacultad(codigo)
        if(pos != None):
            manejaFA.mostrar(pos)
        else:
            print('No se encontró la facultad')
    def opcion2(self, manejaFA):
        carrera = input('Ingrese carrera a buscar: ')
        manejaFA.buscarCarrera(carrera)
    def salir(self):
        print('Saliendo...')