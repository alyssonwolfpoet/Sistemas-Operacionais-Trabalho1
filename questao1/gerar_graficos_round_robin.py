import matplotlib.pyplot as plt

# Dados de exemplo (substituir pelos dados reais)
quantums = [1, 2, 4, 8]
tempos_medio_espera = [13.50, 11.80, 9.70, 7.60]
desvios_espera = [8.29, 7.14, 6.09, 5.14]
tempos_medio_retorno = [18.20, 16.10, 14.30, 12.20]
desvios_retorno = [9.43, 8.36, 7.29, 6.22]

# Gráfico de Tempo Médio de Espera
plt.figure(figsize=(10, 5))
plt.errorbar(quantums, tempos_medio_espera, yerr=desvios_espera, fmt='-o', capsize=5,
             label='Tempo Médio de Espera')
plt.xlabel('Quantum')
plt.ylabel('Tempo Médio de Espera (± std)')
plt.title('Tempo Médio de Espera para Diferentes Valores de Quantum')
plt.legend()
plt.grid(True)
plt.savefig('tempo_medio_espera.png')
plt.show()

# Gráfico de Tempo Médio de Retorno
plt.figure(figsize=(10, 5))
plt.errorbar(quantums, tempos_medio_retorno, yerr=desvios_retorno, fmt='-o', capsize=5,
             label='Tempo Médio de Retorno')
plt.xlabel('Quantum')
plt.ylabel('Tempo Médio de Retorno (± std)')
plt.title('Tempo Médio de Retorno para Diferentes Valores de Quantum')
plt.legend()
plt.grid(True)
plt.savefig('tempo_medio_retorno.png')
plt.show()
