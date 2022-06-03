from ClaseAparato import Aparato

class Lavarropa(Aparato):
    
    __capacidad = ''
    __velocidad = int
    __cantProg = int
    __carga = ''
    
    def __init__(self, marca, modelo, color, pais, precioBase, capacidad, velocidad, cantidadProgramas, carga):
        super().__init__(marca, modelo, color, pais, precioBase)
        self.__capacidad = capacidad
        self.__velocidad = velocidad
        self.__cantProg = cantidadProgramas
        self.__carga = carga
        
    def getCarga(self):
        return self.__carga
    
    def calcPrecioVenta(self):
        precioVenta = super().getPrecio()
        if(self.__capacidad <= 5):
            precioVenta = precioVenta * 1.01
        else:
            precioVenta = precioVenta * 1.03
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
                velocidad = self.__velocidad,
                cantidadProgramas = self.__cantProg,
                carga = self.__carga
                )
            )
        return d