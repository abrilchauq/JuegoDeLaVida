class Celula: 
    def __init__(self, x, y, estaVivo):
        self.x = x
        self.y = y 
        self.vecinas = []
        self.estaVivo = estaVivo

    def agregarCelula(self, celula):
        if len(self.vecinas) <= 8:
            self.vecinas.append(celula)
        else: 
            print('No se puede agregar a la lista')

    def cuantasHay(self):
        cantidad = filter(lambda x: x.estaVivo == True, self.vecinas)
        return(len(list(cantidad)))