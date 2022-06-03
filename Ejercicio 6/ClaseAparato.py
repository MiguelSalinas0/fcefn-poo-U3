class Aparato:
    
    __marca = ''
    __modelo = ''
    __color =''
    __pais = ''
    __precioBase = float
    __precioDeVenta = 0.0
    
    def __init__(self,marca,modelo,color,pais,precioBase):
        self.__marca = marca
        self.__modelo = modelo
        self.__color = color
        self.__pais = pais
        self.__precioBase = precioBase
        self.__precioDeVenta = precioBase
    
    def getMarca(self):
        return self.__marca
    
    def getModelo(self):
        return self.__modelo
    
    def getColor(self):
        return self.__color
    
    def getPais(self):
        return self.__pais
    
    def getPrecio(self):
        return self.__precioBase
    
    def getPrecioVenta(self):
        return self.__precioDeVenta
    
    def setPrecioVenta(self,precio):
        self.__precioDeVenta = precio