import matplotlib.pyplot as plt
import numpy as np

# Dados simulados (exemplo)
num_execucoes = 1000
impasses = np.zeros(num_execucoes)  # Considerando que não houve impasses

# Plotando gráfico
plt.figure(figsize=(10, 5))
plt.plot(impasses, label='Frequência de Impasses')
plt.xlabel('Execuções')
plt.ylabel('Número de Impasses')
plt.title('Frequência de Impasses nas Execuções dos Filósofos')
plt.legend()
plt.grid(True)
plt.savefig('grafico_impasses.png')
plt.show()
