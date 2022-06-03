from ClasePersonal import Personal

class Docente(Personal):
    
    __carrera = ''
    __cargo = ''
    __catedra = ''
    
    def __init__(self,cuil,apellido,nombre,sueldoBasico,antiguedad, carrera, cargo, catedra, area='', tipo='', categoria=''):
        super().__init__(cuil, apellido, nombre, sueldoBasico, antiguedad, carrera, cargo, catedra, area, tipo, categoria)
        self.__carrera = carrera
        self.__cargo = cargo
        self.__catedra = catedra
    
    def getCarrera(self):
        return self.__carrera
    
    def getCargo(self):
        return self.__cargo
    
    def getCatedra(self):
        return self.__catedra
    
    def getSueldo(self):
        return super().getSueldo()
    
    def calcularSueldo(self):
        sueldoFinal = 0.0
        if(self.__cargo.lower() == 'simple'):
            sueldoFinal += super().getSueldoBasico() * 0.10
        if(self.__cargo.lower() == 'semiexclusivo'):
            sueldoFinal += super().getSueldoBasico() * 0.20
        if(self.__cargo.lower() == 'exclusivo'):
            sueldoFinal += super().getSueldoBasico() * 0.50
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
                carrera = self.__carrera,
                cargo = self.__cargo,
                catedra = self.__catedra
                )
            )
        return d