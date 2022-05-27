from ClaseCalefactor import Calefactor

class Electrico(Calefactor):
    
    __potencia = int
    
    def __init__(self,marca,modelo,potencia):
        super().__init__(marca, modelo)
        self.__potencia = potencia
    
    def getPotencia(self):
        return self.__potencia
    
    def calcularConsumo(self,precio,cant):
        consumo = (self.__potencia / 1000) * cant * precio
        super().setConsumo(consumo)