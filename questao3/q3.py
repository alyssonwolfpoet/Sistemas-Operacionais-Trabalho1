import matplotlib.pyplot as plt
import numpy as np

# Exemplo para gráficos de impasses
num_execucoes = 1000
impasses = np.zeros(num_execucoes)

plt.figure(figsize=(10, 5))
plt.plot(impasses, label='Frequência de Impasses')
plt.xlabel('Execuções')
plt.ylabel('Número de Impasses')
plt.title('Frequência de Impasses nas Execuções dos Filósofos')
plt.legend()
plt.grid(True)
plt.savefig('grafico_impasses.png')
plt.show()

# Gráfico de comparação entre as soluções
espera_escritores_solucao1 = np.random.randint(1, 100, num_execucoes)
espera_escritores_solucao2 = np.random.randint(1, 50, num_execucoes)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(espera_escritores_solucao1, label='Solução 1 - Escritores Esperam')
plt.xlabel('Execuções')
plt.ylabel('Tempo de Espera')
plt.title('Tempo de Espera dos Escritores - Solução 1')
plt.legend()
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(espera_escritores_solucao2, label='Solução 2 - Espera Indefinida Resolvida')
plt.xlabel('Execuções')
plt.ylabel('Tempo de Espera')
plt.title('Tempo de Espera dos Escritores - Solução 2')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig('comparacao_solucoes.png')
plt.show()
