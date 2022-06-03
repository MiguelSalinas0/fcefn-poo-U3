from ClaseDocente import Docente
from ClaseInvestigador import Investigador

class DocenteInvestigador(Docente, Investigador):
    
    __categoriaInv = ''
    __importeExtra = 0.0
    
    def __init__(self,cuil,apellido,nombre,sueldoBasico,antiguedad, carrera, cargo, catedra, area, tipo, categoriaInv, importeExtra, categoria=''):
        super().__init__(cuil, apellido, nombre, sueldoBasico, antiguedad, carrera, cargo, catedra, area, tipo, categoria)
        self.__categoriaInv = categoriaInv
        self.__importeExtra = importeExtra
    
    def getCategoriaInv(self):
        return self.__categoriaInv
    
    def getExtra(self):
        return self.__importeExtra
    
    def calcularSueldo(self):
        Docente.calcularSueldo(self)
        sd = Docente.getSueldo(self)
        sueldo = sd + self.__importeExtra
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
                carrera = self.getCarrera(),
                cargo = self.getCargo(),
                catedra = self.getCatedra(),
                area = self.getArea(),
                tipo = self.getTipo(),
                categoriaInv = self.__categoriaInv,
                importeExtra = self.__importeExtra
                )
            )
        return d