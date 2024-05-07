import random

class Dado:
    def __init__(self):
        self.valor = None

    def tirar(self):
        self.valor = random.randint(1, 6)

    def __str__(self):
        return str(self.valor)

