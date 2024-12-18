import matplotlib.pyplot as plt
import numpy as np

# Dados simulados
num_execucoes = 1000
espera_escritores_solucao1 = np.random.randint(1, 100, num_execucoes)
espera_escritores_solucao2 = np.random.randint(1, 50, num_execucoes)

# Plotando gráficos
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(espera_escritores_solucao1, label='Solução 1 - Escritores Esperam')
plt.xlabel('Execuções')
plt.ylabel('Tempo de Espera')
plt.title('Tempo de Espera dos Escritores - Solução 1')
plt.legend()
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(espera_escritores_solucao2, label='Solução 2 - Espera Resolvida')
plt.xlabel('Execuções')
plt.ylabel('Tempo de Espera')
plt.title('Tempo de Espera dos Escritores - Solução 2')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.savefig('comparacao_solucoes.png')
plt.show()
