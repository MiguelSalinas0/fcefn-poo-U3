class Jugador:
    
    __nombre = ''
    __dni = ''
    __ciudadNatal = ''
    __pais = ''
    __fechaNacimiento = ''
    __contratos = []
    
    def __init__(self,nom,dni,ciudad,pais,fecha):
        self.__nombre = nom
        self.__dni = dni
        self.__ciudadNatal = ciudad
        self.__pais = pais
        self.__fechaNacimiento = fecha
        self.__contratos = []
    
    def getNombre(self):
        return self.__nombre
    
    def getDNI(self):
        return self.__dni
    
    def getCiudadNatal(self):
        return self.__ciudadNatal
    
    def getPais(self):
        return self.__pais
    
    def getFechaNacimiento(self):
        return self.__fechaNacimiento
    
    def agregarContrato(self, contrato):
        self.__contratos.append(contrato)
    
    def __str__(self):
        cadena = 'Nombre jugador: ' + str(self.__nombre)
        return cadena
    