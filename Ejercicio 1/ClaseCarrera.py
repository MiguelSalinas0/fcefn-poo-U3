class Carrera:
    
    __codigo = int
    __nombre = ''
    __titulo = ''
    __duracion = ''
    __categoria = ''
    
    def __init__(self, cod, nom, titulo, duracion, categoria):
        self.__codigo = cod
        self.__nombre = nom
        self.__titulo = titulo
        self.__duracion = duracion
        self.__categoria = categoria
        
    def getCodigo(self):
        return self.__codigo
    
    def getNombre(self):
        return self.__nombre
    
    def getTitulo(self):
        return self.__titulo
    
    def getDuracion(self):
        return self.__duracion
    
    def getCategoria(self):
        return self.__categoria
    