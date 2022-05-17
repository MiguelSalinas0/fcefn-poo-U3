from ClaseCarrera import Carrera

class Facultad:
    
    __codigo = int
    __nombre = ''
    __direccion = ''
    __localidad = ''
    __telefono = ''
    __carreras = []
    
    def __init__(self, cod, nom, direccion, localidad, tel, carreras = []):
        self.__codigo = cod
        self.__nombre = nom
        self.__direccion = direccion
        self.__localidad = localidad
        self.__telefono = tel
        self.__carreras = []
        for i in carreras:
            codC = i[1]
            nomC = i[2]
            titC = i[3]
            duracionC = i[4]
            categoriaC = i[5]
            nuevaCarrera = Carrera(codC, nomC, titC, duracionC, categoriaC)
            self.__carreras.append(nuevaCarrera)
    
    def getCodigo(self):
        return self.__codigo
    
    def getNombre(self):
        return self.__nombre
    
    def getCarrera(self, carrera):
        pos = 0
        bandera = False
        while(pos < len(self.__carreras) and bandera == False):
            if(self.__carreras[pos].getNombre().lower() == carrera.lower()):
                print('\nCódigo de carrera: {}{}'.format(self.__codigo, self.__carreras[pos].getCodigo()))
                print('Facultad: {}'.format(self.__nombre))
                print('Dirección: {}'.format(self.__direccion))
                bandera = True
            else:
                pos += 1
        return bandera
    
    def mostrarFacultad(self):
        print('\nFacultad: {}'.format(self.__nombre))
        for item in self.__carreras:
            print('Carrera: {}, | Duración: {}'.format(item.getNombre(), item.getDuracion()))
            