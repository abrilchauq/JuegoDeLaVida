from celula import Celula


class Tablero:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.celulas = []

    def agregarCell(self):
        for columna in range(self.y):
            for fila in range(self.x):
                self.celulas.append(Celula(fila, columna, False))

