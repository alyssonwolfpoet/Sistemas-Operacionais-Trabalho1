import random
import matplotlib.pyplot as plt

# Função para calcular o tempo de espera e o tempo de retorno
def round_robin(processes, quantum):
    n = len(processes)
    burst_times = [p[1] for p in processes]
    waiting_times = [0] * n
    turnaround_times = [0] * n
    remaining_burst = burst_times[:]
    queue = list(range(n))
    time = 0

    while queue:
        current = queue.pop(0)
        if remaining_burst[current] > quantum:
            remaining_burst[current] -= quantum
            time += quantum
            queue.append(current)
        else:
            time += remaining_burst[current]
            waiting_times[current] = time - burst_times[current]
            turnaround_times[current] = time
            remaining_burst[current] = 0
    
    avg_waiting_time = sum(waiting_times) / n
    avg_turnaround_time = sum(turnaround_times) / n
    throughput = n / time  # Processos concluídos por unidade de tempo
    
    return avg_waiting_time, avg_turnaround_time, throughput

# Gerar dados aleatórios para os processos
def generate_processes(num_processes, burst_time_range=(1, 10)):
    return [(f'P{i+1}', random.randint(burst_time_range[0], burst_time_range[1])) for i in range(num_processes)]

# Parâmetros
num_processes = 10
quantum_values = [2, 4, 6, 8, 10]

# Armazenar resultados para diferentes valores de quantum
waiting_times = []
turnaround_times = []
throughputs = []

for quantum in quantum_values:
    processes = generate_processes(num_processes)
    avg_waiting, avg_turnaround, throughput = round_robin(processes, quantum)
    waiting_times.append(avg_waiting)
    turnaround_times.append(avg_turnaround)
    throughputs.append(throughput)

# Plotar resultados
plt.figure(figsize=(10, 6))
plt.subplot(3, 1, 1)
plt.plot(quantum_values, waiting_times, label='Tempo Médio de Espera', marker='o')
plt.xlabel('Quantum')
plt.ylabel('Tempo Médio de Espera')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(quantum_values, turnaround_times, label='Tempo Médio de Retorno', marker='o', color='g')
plt.xlabel('Quantum')
plt.ylabel('Tempo Médio de Retorno')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(quantum_values, throughputs, label='Vazão', marker='o', color='r')
plt.xlabel('Quantum')
plt.ylabel('Vazão')
plt.grid(True)

plt.tight_layout()
plt.show()
