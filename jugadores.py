class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntaje_total = 0
        self.puntaje_ronda = 0

    def reiniciar_puntaje_ronda(self):
        self.puntaje_ronda = 0

    def sumar_puntaje_ronda(self, puntaje):
        self.puntaje_ronda += puntaje

    def actualizar_puntaje_total(self):
        self.puntaje_total += self.puntaje_ronda

    def __str__(self):
        return f"{self.nombre} - Puntaje Total: {self.puntaje_total}"
