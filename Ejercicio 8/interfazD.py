from zope.interface import interface
class IDirector(interface):
    def ModificarBasico(dni,nuevoBasico):
        pass
    def modificarPorcentajeporcargo(dni,nuevoPorcentaje):
        pass
    def modificarPorcentajeporcategoria(dn,nuevoPorcentaje):
        pass
    def modificaImporteExtra(dni,nuevoImporteExtra):
        pass