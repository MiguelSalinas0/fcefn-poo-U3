class Ramo:
    
    __listaFlores = []
    
    def __init__(self):
        self.__listaFlores = []
        
    def agregarFlor(self, flor, cantidad):
        for i in range(cantidad):
            self.__listaFlores.append(flor)
        
    