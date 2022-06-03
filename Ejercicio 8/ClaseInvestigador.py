from ClasePersonal import Personal

class Investigador(Personal):
    
    __area = ''
    __tipo = ''
    
    def __init__(self,cuil,apellido,nombre,sueldoBasico,antiguedad, carrera='', cargo='', catedra='', area='', tipo='', categoria=''):
        super().__init__(cuil, apellido, nombre, sueldoBasico, antiguedad, carrera, cargo, catedra, area, tipo, categoria)
        self.__area = area
        self.__tipo = tipo
    
    def getArea(self):
        return self.__area
    
    def getTipo(self):
        return self.__tipo
    
    def calcularSueldo(self):
        antiguedad = (super().getSueldoBasico() * super().getAntiguedad()) / 100
        sueldo = super().getSueldoBasico() + antiguedad
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
                area = self.__area,
                tipo = self.__tipo
                )
            )
        return d
    