import matplotlib.pyplot as plt

def round_robin(processes, burst_times, quantum):
    n = len(processes)
    remaining_times = burst_times[:]
    waiting_times = [0] * n
    turnaround_times = [0] * n
    sequence = []

    time = 0
    while True:
        done = True
        for i in range(n):
            if remaining_times[i] > 0:
                done = False
                sequence.append(processes[i])
                if remaining_times[i] > quantum:
                    time += quantum
                    remaining_times[i] -= quantum
                else:
                    time += remaining_times[i]
                    waiting_times[i] = time - burst_times[i]
                    remaining_times[i] = 0
        if done:
            break

    for i in range(n):
        turnaround_times[i] = burst_times[i] + waiting_times[i]

    avg_wait = sum(waiting_times) / n
    avg_turnaround = sum(turnaround_times) / n

    return sequence, avg_wait, avg_turnaround


def plot_results(processes, burst_times, quantum, sequence):
    plt.figure(figsize=(10, 6))
    plt.bar(processes, burst_times, color='skyblue')
    plt.title(f"Round Robin Scheduling (Quantum={quantum})")
    plt.xlabel("Processes")
    plt.ylabel("Burst Time")
    plt.grid()
    plt.savefig("resultados.png")
    plt.show()


if __name__ == "__main__":
    processes = ["P1", "P2", "P3", "P4"]
    burst_times = [10, 5, 8, 12]
    quantum = 3

    sequence, avg_wait, avg_turnaround = round_robin(processes, burst_times, quantum)

    print("Ordem de execução:", " -> ".join(sequence))
    print("Tempo médio de espera:", avg_wait)
    print("Tempo médio de retorno:", avg_turnaround)

    plot_results(processes, burst_times, quantum, sequence)
