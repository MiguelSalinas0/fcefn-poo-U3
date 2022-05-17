class Flor:
    
    __numero = int
    __nombre = ''
    __color = ''
    __descripcion = ''
    __cantV = int
    
    def __init__(self,num,nom,color,descr):
        self.__numero = num
        self.__nombre = nom
        self.__color = color
        self.__descripcion = descr
        self.__cantV = 0
    
    def getNumero(self):
        return self.__numero
    
    def getNombre(self):
        return self.__nombre
    
    def getColor(self):
        return self.__color
    
    def getDescripcion(self):
        return self.__descripcion
    
    def getCant(self):
        return self.__cantV
    
    def setCant(self, cant):
        self.__cantV += cant
    
    def __gt__(self, otro):
        if(self.__cantV > otro.__cantV):
            return False
        else:
            return True