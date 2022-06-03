from ClaseHeladera import Heladera
from ClaseTelevisor import Televisor
from ClaseLavarropa import Lavarropa

class Menu:
    
    __switcher = None
    
    def __init__(self):
        self.__switcher = {'1':self.opcion1,
                           '2':self.opcion2,
                           '3':self.opcion3,
                           '4':self.opcion4,
                           '5':self.opcion5,
                           '6':self.opcion6,
                           '7':self.opcion7,
                           '8':self.salir
                           }
    
    def opcion(self,op,lista,jsonF):
        func = self.__switcher.get(op, lambda: print('Opción no válida'))
        if(op=='1' or op=='2' or op=='3' or op=='4' or op=='5' or op=='6' or op=='7'):
            func(lista,jsonF)
        else:
            func()
            
    def opcion1(self,lista,jsonF):
        tipo = input('Ingrese el tipo de aparato que desea insertar: ')
        aparato = self.crearAparato(tipo)
        pos = int(input('\nIngrese la posición en la que desea insertar el aparato: '))
        band = lista.insertarAparato(aparato, pos)
        if(band == True):
            print('\nSe pudo insertar el elemento')
        else:
            print('\nNo se pudo insertar el elemento')
    
    def opcion2(self, lista,jsonF):
        tipo = input('Ingrese el tipo de aparato: ')
        aparato = self.crearAparato(tipo)
        lista.agregarAparato(aparato)
    
    def opcion3(self,lista,jsonF):
        pos = int(input('Ingrese una posición para visualizar el aparato que se encuentra: '))
        lista.mostrarPos(pos)
    
    def opcion4(self,lista,jsonF):
        cant = lista.cuentaMarca()
        print('Cantidad total: {}'.format(cant))
    
    def opcion5(self,lista,jsonF):
        lista.cantCargSup()
    
    def opcion6(self,lista,jsonF):
        lista.mostrarPrecioVenta()
    
    def opcion7(self,lista,jsonF):
        d = lista.toJSON()
        jsonF.guardarJSONArchivo(d,'aparatoselectronicos.json')
    
    def salir(self):
        print('Saliendo...')
    
    def crearAparato(self, tipo):
        aparato = None
        marca = input('Ingrese la marca: ')
        modelo = input('Ingrese el modelo: ')
        color = input('Ingrese el color: ')
        pais = input('Ingrese el país de fabricación: ')
        precio = float(input('Ingrese el precio base: '))
        if(tipo.lower() == 'heladera'):
            capacidad = int(input('Ingrese la capacidad en litros: '))
            freezer = input('Ingrese si posee freezer: ')
            if(freezer.lower() == 'si'):
                fre = True
            else:
                fre = False
            ciclica = input('Ingrese si es ciclica: ')
            if(ciclica.lower() == 'si'):
                cic = True
            else:
                cic = False
            aparato = Heladera(marca, modelo, color, pais, precio, capacidad, fre, cic)
        if(tipo.lower() == 'televisor'):
            pantalla = input('Ingrese el tipo de pantalla: ')
            pulgadas = int(input('Ingrese la cantidad de pulgadas: '))
            definicion = input('Ingrese el tipo de definición: ')
            internet = input('Ingrese si posee internet: ')
            if(internet.lower() == 'si'):
                inter = True
            else:
                inter = False
            aparato = Televisor(marca, modelo, color, pais, precio, pantalla, pulgadas, definicion, inter)
        if(tipo.lower() == 'lavarropas'):
            carga = int(input('Ingrese cantidad de carga: '))
            velocidad = int(input('Ingrese la velocidad de centrifugado: '))
            cantProg = int(input('Ingrese la cantidad de programas: '))
            Tcarga = input('Ingrese el tipo de carga: ')
            aparato = Lavarropa(marca, modelo, color, pais, precio, carga, velocidad, cantProg, Tcarga)
        return aparato