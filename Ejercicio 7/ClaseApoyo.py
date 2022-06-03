from ClasePersonal import Personal

class Apoyo(Personal):
    
    __categoria = 0
    
    def __init__(self,cuil,apellido,nombre,sueldoBasico,antiguedad, categoria, carrera='', cargo='', catedra='', area='', tipo=''):
        super().__init__(cuil, apellido, nombre, sueldoBasico, antiguedad, carrera, cargo, catedra, area, tipo, categoria)
        self.__categoria = categoria
    
    def calcularSueldo(self):
        sueldoFinal = 0.0
        if(1 <= self.__categoria <= 10):
            sueldoFinal += super().getSueldoBasico() * 0.10
        if(11 <= self.__categoria <= 20):
            sueldoFinal += super().getSueldoBasico() * 0.20
        if(21 <= self.__categoria <= 22):
            sueldoFinal += super().getSueldoBasico() * 0.30
        antiguedad = (super().getSueldoBasico() * super().getAntiguedad()) / 100
        sueldo = super().getSueldoBasico() + antiguedad + sueldoFinal
        super().setSueldo(sueldo)
    
    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                cuil = self.getCuil(),
                apellido = self.getApellido(),
                nombre = self.getNombre(),
                sueldoBasico = self.getSueldoBasico(),
                antiguedad = self.getAntiguedad(),
                categoria = self.__categoria
                )
            )
        return d