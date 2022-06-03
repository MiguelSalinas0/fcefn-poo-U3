from ClaseDocente import Docente
from ClaseInvestigador import Investigador
from ClaseDocenteInvestigador import DocenteInvestigador
from ClaseApoyo import Apoyo

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
                           '8':self.opcion8,
                           '9':self.salir
                           }
    def opcion(self,op,lista,jsonF):
        func = self.__switcher.get(op, lambda: print('Opción no válida'))
        if(op=='1' or op=='2' or op=='3' or op=='4' or op=='5' or op=='6' or op=='7' or op=='8'):
            func(lista,jsonF)
        else:
            func()
    
    def opcion1(self,lista,jsonF):
        agente = self.carga()
        pos = int(input('\nIngrese la posición en la que desea insertar al agente: '))
        ban = lista.insertar(agente,pos)
        if(ban == True):
            print('\nSe pudo insertar el agente')
        else:
            print('\nNo se pudo insertar el agente')
    
    def opcion2(self, lista,jsonF):
        agente = self.carga()
        lista.agregarPersonal(agente)
    
    def opcion3(self, lista,jsonF):
        pos = int(input('Ingrese una posición para visualizar el personal que se encuentra: '))
        lista.mostrarPos(pos)
    
    def opcion4(self, lista,jsonF):
        carrera = input('Ingrese el nombre de una carrera: ')
        lista.ordenarPorNombre()
        lista.mostrar4(carrera)
    
    def opcion5(self,lista,jsonF):
        area = input('\nIngrese el nombre de área: ')
        lista.contarDyDI(area)
    
    def opcion6(self,lista,jsonF):
        lista.ordenarPorApellido()
        lista.mostrar6()
        
    def opcion7(self,lista,jsonF):
        categoria = input('\nIngrese categoría de investigación: ')
        lista.listarDI(categoria)
    
    def opcion8(self,lista,jsonF):
        d = lista.toJSON()
        jsonF.guardarJSONArchivo(d, 'personal.json')
        
    def salir(self):
        print('Saliendo...')
    
    def carga(self):
        objeto = None
        tipo = input('\nIngrese el tipo de agente que desea cargar: ')
        cuil = input('\nIngrese cuil: ')
        nombre = input('Ingrese nombre: ')
        apellido = input('Ingrese apellido: ')
        sueldoBasico = float(input('Ingrese sueldo basico: '))
        antiguedad = int(input('Ingrese años de antiguedad: '))
        if(tipo.lower() == 'docente'):
            carrera = input('Ingrese carrera en la que dicta clases: ')
            cargo = input('Ingrese cargo: ')
            catedra = input('Ingrese cátedra: ')
            docente = Docente(cuil, apellido, nombre, sueldoBasico, antiguedad, carrera, cargo, catedra)
            objeto = docente
        if(tipo.lower() == 'investigador'):
            area = input('Ingrese área de investigación: ')
            tipo = input('Ingrese el tipo de investigación: ')
            investigador = Investigador(cuil, apellido, nombre, sueldoBasico, antiguedad,'','','',area,tipo)
            objeto = investigador
        if(tipo.lower() == 'docente investigador'):
            carrera = input('Ingrese carrera en la que dicta clases: ')
            cargo = input('Ingrese cargo: ')
            catedra = input('Ingrese cátedra: ')
            area = input('Ingrese área de investigación: ')
            tipo = input('Ingrese el tipo de investigación: ')
            categoriaInv = input('Ingrese la categoría en el programa de incentivos: ')
            importeExtra = float(input('Ingrese el importe extra: '))
            docenteInvestigador = DocenteInvestigador(cuil, apellido, nombre, sueldoBasico, antiguedad, carrera, cargo, catedra, area, tipo, categoriaInv, importeExtra)
            objeto = docenteInvestigador
        if(tipo.lower() == 'apoyo'):
            categoria = input('Ingrese categoría del personal de apoyo: ')
            apoyo = Apoyo(cuil, apellido, nombre, sueldoBasico, antiguedad, categoria)
            objeto = apoyo
        return objeto