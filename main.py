from jugadores import Jugador
from marcador import Marcador
from interfaz import mostrar_mensaje, solicitar_entrada
from dados import Dado

def main():
    jugador1 = Jugador("Jugador 1")
    jugador2 = Jugador("Jugador 2")
    marcador = Marcador(jugador1, jugador2)

    for ronda in range(1, 4):
        mostrar_mensaje(f"Ronda {ronda}")
        for turno in range(1, 4):
            mostrar_mensaje(f"Turno {turno}")

            
            mostrar_mensaje(f"Turno del {jugador1.nombre}")
            jugar_turno(jugador1, marcador)
            mostrar_mensaje(f"Turno del {jugador2.nombre}")
            jugar_turno(jugador2, marcador)

            
            jugador1.reiniciar_puntaje_ronda()
            jugador2.reiniciar_puntaje_ronda()

    marcador.mostrar_resultados_finales()

def jugar_turno(jugador, marcador):
    dados = [Dado() for _ in range(5)]
    for _ in range(3):
        mostrar_mensaje(f"{jugador.nombre}, lanzando dados...")
        for dado in dados:
            dado.tirar()
            mostrar_mensaje(f"Dado: {dado}")

        mostrar_mensaje("Selecciona los dados que deseas guardar (ej. 1 3 5) o 'ninguno' para lanzar de nuevo:")
        seleccion = solicitar_entrada(">> ")
        if seleccion.lower() == "ninguno":
            for dado in dados:
                dado.tirar()
        else:
            seleccion = [int(num) - 1 for num in seleccion.split()]
            for i, dado in enumerate(dados):
                if i not in seleccion:
                    dado.tirar()

        mostrar_mensaje("Elige una combinación para anotar (Generala, Poker, Full, Escalera, Color, Trío, Dos pares, Par):")
        combinacion = solicitar_entrada(">> ")
        puntaje = marcador.calcular_puntaje(combinacion, dados)
        mostrar_mensaje(f"Puntaje obtenido: {puntaje}")
        jugador.sumar_puntaje_ronda(puntaje)

if __name__ == "__main__":
    main()
