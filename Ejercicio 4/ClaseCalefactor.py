class Calefactor:
    
    __marca = ''
    __modelo = ''
    __consumo = int
    
    def __init__(self,marca,modelo):
        self.__marca = marca
        self.__modelo = modelo
        self.__consumo = 0
        
    def getMarca(self):
        return self.__marca
    
    def getModelo(self):
        return self.__modelo
    
    def calcularConsumo(self,costoM3,cant):
        pass
    
    def setConsumo(self,consumo):
        self.__consumo = consumo
    
    def getConsumo(self):
        return self.__consumo