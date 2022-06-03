from ClaseAparato import Aparato

class Televisor(Aparato):
    
    __tipoPantalla = ''
    __pulgadas = int
    __tipoDefinicion = ''
    __internet = bool
    
    def __init__(self, marca, modelo, color, pais, precioBase, pantalla, pulgadas, definicion, internet):
        super().__init__(marca, modelo, color, pais, precioBase)
        self.__tipoPantalla = pantalla
        self.__pulgadas = pulgadas
        self.__tipoDefinicion = definicion
        self.__internet = internet
        
    def calcPrecioVenta(self):
        precioVenta = super().getPrecio()
        if(self.__tipoDefinicion.lower() == 'sd'):
            precioVenta = precioVenta * 1.01
        if(self.__tipoDefinicion.lower() == 'hd'):
            precioVenta = precioVenta * 1.02
        if(self.__tipoDefinicion.lower() == 'full hd'):
            precioVenta = precioVenta * 1.03
        if(self.__internet == True):
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
                pantalla = self.__tipoPantalla,
                pulgadas = self.__pulgadas,
                definicion = self.__tipoDefinicion,
                internet = self.__internet
                )
            )
        return d