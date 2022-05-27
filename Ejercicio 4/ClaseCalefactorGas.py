from ClaseCalefactor import Calefactor

class Gas(Calefactor):
    
    __matricula = ''
    __calorias = int
    
    def __init__(self, marca, modelo, matricula, calorias):
        super().__init__(marca, modelo)
        self.__matricula = matricula
        self.__calorias = calorias
    
    def getMatricula(self):
        return self.__matricula
    
    def getCalorias(self):
        return self.__calorias
    
    def calcularConsumo(self,precio,cant):
        consumo = (self.__calorias / 1000) * cant * precio
        super().setConsumo(consumo)