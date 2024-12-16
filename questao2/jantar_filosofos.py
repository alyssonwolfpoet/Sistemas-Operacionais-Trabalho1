import threading
import time
import random

class Filosofo(threading.Thread):
    def __init__(self, nome, garfo_esquerdo, garfo_direito):
        threading.Thread.__init__(self)
        self.nome = nome
        self.garfo_esquerdo = garfo_esquerdo
        self.garfo_direito = garfo_direito

    def run(self):
        for _ in range(10):  # Cada filósofo tenta comer 10 vezes
            self.pensar()
            self.pegar_garfos()
            self.comer()
            self.soltar_garfos()

    def pensar(self):
        print(f"{self.nome} está pensando.")
        time.sleep(random.uniform(1, 3))

    def pegar_garfos(self):
        # Estratégia: sempre tentar pegar o garfo esquerdo primeiro
        garfos = sorted([self.garfo_esquerdo, self.garfo_direito], key=lambda x: id(x))
        with garfos[0]:
            with garfos[1]:
                print(f"{self.nome} pegou os garfos e está pronto para comer.")

    def comer(self):
        print(f"{self.nome} está comendo.")
        time.sleep(random.uniform(1, 2))

    def soltar_garfos(self):
        print(f"{self.nome} soltou os garfos.")


def jantar_dos_filosofos():
    n_filosofos = 5
    garfos = [threading.Lock() for _ in range(n_filosofos)]

    filosofos = [
        Filosofo(f"Filósofo {i+1}", garfos[i], garfos[(i+1) % n_filosofos])
        for i in range(n_filosofos)
    ]

    for filosofo in filosofos:
        filosofo.start()

    for filosofo in filosofos:
        filosofo.join()


if __name__ == "__main__":
    jantar_dos_filosofos()
