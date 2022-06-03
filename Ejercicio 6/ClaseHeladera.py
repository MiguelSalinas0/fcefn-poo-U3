from ClaseAparato import Aparato

class Heladera(Aparato):
    
    __capacidad = int
    __freezer = bool
    __ciclica = bool
    
    def __init__(self, marca, modelo, color, pais, precioBase, capacidad, freezer, ciclica):
        super().__init__(marca, modelo, color, pais, precioBase)
        self.__capacidad = capacidad
        self.__freezer = freezer
        self.__ciclica = ciclica
    
    def calcPrecioVenta(self):
        precioVenta = super().getPrecio()
        if(self.__freezer == False):
            precioVenta = precioVenta * 1.01
        if(self.__freezer == True):
            precioVenta = precioVenta * 1.05
        if(self.__ciclica == True):
            precioVenta = precioVenta * 1.10
        precioVenta = round(precioVenta,1)
        super().setPrecioVenta(precioVenta)
    
    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                marca = self.getMarca(),
                modelo = self.getModelo(),
                color = self.getColor(),
                pais = self.getPais(),
                precioBase = self.getPrecio(),
                capacidad = self.__capacidad,
                freezer = self.__freezer,
                ciclica = self.__ciclica
                )
            )
        return d