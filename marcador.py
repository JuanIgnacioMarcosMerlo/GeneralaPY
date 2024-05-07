class Marcador:
    def __init__(self, jugador1, jugador2):
        self.jugador1 = jugador1
        self.jugador2 = jugador2

    
    def calcular_puntaje(self, combinacion, dados):
        puntaje = 0

        if combinacion == "Generala":
            if self.es_generala(dados):
                puntaje = 50
        elif combinacion == "Poker":
            if self.es_poker(dados):
                puntaje = 40
        elif combinacion == "Full":
            if self.es_full(dados):
                puntaje = 30
        elif combinacion == "Escalera":
            if self.es_escalera(dados):
                puntaje = 20
        elif combinacion == "Color":
            if self.es_color(dados):
                puntaje = 20
        elif combinacion == "Trío":
            if self.es_trio(dados):
                puntaje = 10
        elif combinacion == "Dos pares":
            if self.es_dos_pares(dados):
                puntaje = 5
        elif combinacion == "Par":
            if self.es_par(dados):
                puntaje = 1

        return puntaje

    def es_generala(self, dados):
        valores = [dado.valor for dado in dados]
        return valores.count(valores[0]) == 5

    def es_poker(self, dados):
        valores = [dado.valor for dado in dados]
        return max(valores.count(valor) for valor in set(valores)) >= 4

    def es_full(self, dados):
        valores = [dado.valor for dado in dados]
        return max(valores.count(valor) for valor in set(valores)) == 3 and len(set(valores)) == 2

    def es_escalera(self, dados):
        valores = sorted([dado.valor for dado in dados])
        return valores in [[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]

    def es_color(self, dados):
        colores = [dado.color for dado in dados]
        return len(set(colores)) == 1

    def es_trio(self, dados):
        valores = [dado.valor for dado in dados]
        return max(valores.count(valor) for valor in set(valores)) >= 3

    def es_dos_pares(self, dados):
        valores = [dado.valor for dado in dados]
        return len(set(valores)) == 3 and max(valores.count(valor) for valor in set(valores)) >= 2

    def es_par(self, dados):
        valores = [dado.valor for dado in dados]
        return max(valores.count(valor) for valor in set(valores)) >= 2

    def mostrar_resultados_finales(self):
        print("Resultados finales:")
        print(self.jugador1)
        print(self.jugador2)
        if self.jugador1.puntaje_total > self.jugador2.puntaje_total:
            print(f"{self.jugador1.nombre} gana!")
        elif self.jugador1.puntaje_total < self.jugador2.puntaje_total:
            print(f"{self.jugador2.nombre} gana!")
        else:
            print("¡Empate!")
