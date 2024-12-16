import threading
import time
import random

class LeitoresEscritores:
    def __init__(self):
        self.leitores = 0
        self.mutex_leitores = threading.Lock()
        self.regiao_critica = threading.Lock()

    def leitor(self, id_leitor):
        while True:
            with self.mutex_leitores:
                self.leitores += 1
                if self.leitores == 1:
                    self.regiao_critica.acquire()
            print(f"Leitor {id_leitor} está lendo.")
            time.sleep(random.uniform(0.5, 2))
            with self.mutex_leitores:
                self.leitores -= 1
                if self.leitores == 0:
                    self.regiao_critica.release()
            time.sleep(random.uniform(0.5, 1))

    def escritor(self, id_escritor):
        while True:
            print(f"Escritor {id_escritor} está tentando escrever.")
            self.regiao_critica.acquire()
            print(f"Escritor {id_escritor} está escrevendo.")
            time.sleep(random.uniform(1, 3))
            self.regiao_critica.release()
            print(f"Escritor {id_escritor} terminou de escrever.")
            time.sleep(random.uniform(0.5, 2))


def simular_leitores_escritores(num_leitores, num_escritores):
    sistema = LeitoresEscritores()
    threads = []

    for i in range(num_leitores):
        t = threading.Thread(target=sistema.leitor, args=(i + 1,))
        threads.append(t)

    for i in range(num_escritores):
        t = threading.Thread(target=sistema.escritor, args=(i + 1,))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()


if __name__ == "__main__":
    num_leitores = 3
    num_escritores = 2
    simular_leitores_escritores(num_leitores, num_escritores)
