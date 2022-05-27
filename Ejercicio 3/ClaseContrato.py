from datetime import datetime

class Contrato:
    
    __fechaInicio = datetime
    __fechaFin = datetime
    __pagoMensual = float
    __jugador = None
    __equipo = None
    
    def __init__(self,inicio,fin,pago,jugador,equipo):
        self.__fechaInicio = inicio
        self.__fechaFin = fin
        self.__pagoMensual = pago
        self.__jugador = jugador
        self.__equipo = equipo
    
    def getFechaInicio(self):
        return self.__fechaInicio
    
    def getFechaFin(self):
        return self.__fechaFin
    
    def getPagoMensual(self):
        return self.__pagoMensual
    
    def getJugador(self):
        return self.__jugador
    
    def getEquipo(self):
        return self.__equipo
    
    def calcularMeses(self):
        meses = 0
        cantDias = self.__fechaFin - self.__fechaInicio
        meses = round(cantDias.days / 30.4172)
        return meses