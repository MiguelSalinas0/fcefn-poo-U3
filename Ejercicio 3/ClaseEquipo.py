class Equipo:
    
    __ide = int
    __nombre = ''
    __ciudad = ''
    __listaContratos = []
    
    def __init__(self,ide,nom,ciudad):
        self.__ide = ide
        self.__nombre = nom
        self.__ciudad = ciudad
        self.__listaContratos = []
        
    def getID(self):
        return self.__ide
        
    def getNombre(self):
        return self.__nombre
    
    def getCiudad(self):
        return self.__ciudad
    
    def agregarContrato(self,contrato):
        self.__listaContratos.append(contrato)
        
    def __str__(self):
        cadena = '\nNombre Equipo: ' + str(self.__nombre)
        return cadena