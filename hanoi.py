class Pila:
    def __init__(self):
        self.items = []

    def vacia(self):
        return self.items == []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop()


class TorresDeHanoi:
    def __init__(self):
        self.torres = [Pila(), Pila(), Pila()]
        self.movimientos = []
        self.solucion = None
        self.fin_juego = False
        self.disco_seleccionado = None
        self.torre_origen = None

        for i in range(3, 0, -1):
            self.torres[0].apilar(i)

    def seleccionar_torre(self, torre):
        if torre.isdigit() and 0 <= int(torre) < 3:
            return int(torre)
        return None

    def mover_disco(self, origen, destino):
        disco = self.torres[origen].desapilar()
        self.torres[destino].apilar(disco)
        self.movimientos.append((origen, destino))

    def resolver_hanoi(self, n, origen, destino, auxiliar):
        if n == 1:
            self.mover_disco(origen, destino)
        else:
            self.resolver_hanoi(n-1, origen, auxiliar, destino)
            self.mover_disco(origen, destino)
            self.resolver_hanoi(n-1, auxiliar, destino, origen)

    def imprimir_torres(self):
        for i, torre in enumerate(self.torres):
            print(f"Torre {i}: {torre.items}")

    def resolver(self):
        self.solucion = self.movimientos = []
        self.torres = [Pila(), Pila(), Pila()]
        for i in range(3, 0, -1):
            self.torres[0].apilar(i)
        self.resolver_hanoi(3, 0, 2, 1)

    def verificar_fin_juego(self):
        if self.torres[2].items == [3, 2, 1]:
            self.fin_juego = True

    def reiniciar(self):
        self.fin_juego = False
        self.movimientos = []
        self.solucion = None
        self.torres = [Pila(), Pila(), Pila()]
        for i in range(3, 0, -1):
            self.torres[0].apilar(i)


def main():
    juego = TorresDeHanoi()

    while not juego.fin_juego:
        juego.imprimir_torres()
        origen = input("Seleccione la torre de origen (0, 1, 2): ")
        torre_origen = juego.seleccionar_torre(origen)
        if torre_origen is None or juego.torres[torre_origen].vacia():
            print("Torre seleccionada incorrecta o vacía. Inténtelo de nuevo.")
            continue

        destino = input("Seleccione la torre de destino (0, 1, 2): ")
        torre_destino = juego.seleccionar_torre(destino)
        if torre_destino is None or (not juego.torres[torre_destino].vacia() and juego.torres[torre_destino].items[-1] < juego.torres[torre_origen].items[-1]):
            print("Torre seleccionada incorrecta. Inténtelo de nuevo.")
            continue

        juego.mover_disco(torre_origen, torre_destino)
        juego.verificar_fin_juego()

    print("¡Felicidades! Has ganado el juego de las Torres de Hanoi.")


if __name__ == "__main__":
    main()
