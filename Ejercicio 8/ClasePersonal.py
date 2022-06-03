class Personal:

    __cuil = ''
    __apellido = ''
    __nombre = ''
    __sueldoBasico = 0.0
    __antiguedad = 0
    __sueldo = 0.0

    def __init__(self, cuil, apellido, nombre, sueldoBasico, antiguedad, carrera='', cargo='', catedra='', area='', tipo='', categoria=''):
        self.__cuil = cuil
        self.__apellido = apellido
        self.__nombre = nombre
        self.__sueldoBasico = sueldoBasico
        self.__antiguedad = antiguedad
        self.__sueldo = 0
        
    def getCuil(self):
        return self.__cuil
    def setBasico(self,algo):
        self.__sueldoBasico=algo
        
    def getApellido(self):
        return self.__apellido
    
    def getNombre(self):
        return self.__nombre
    
    def getSueldoBasico(self):
        return self.__sueldoBasico
    
    def getAntiguedad(self):
        return self.__antiguedad
    
    def getSueldo(self):
        return self.__sueldo
    
    def setSueldo(self, sueldo):
        self.__sueldo = sueldo