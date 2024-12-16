#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int id;
    int burst_time;
    int tempo_restante;
    int tempo_espera;
    int tempo_retorno;
} Processo;

void escalonamento_round_robin(Processo processos[], int n, int quantum) {
    int tempo_corrente = 0;
    int executado = 0;
    int *fila = (int *)malloc(n * sizeof(int));
    int inicio = 0, fim = 0;

    for (int i = 0; i < n; i++) {
        fila[fim++] = i;
        processos[i].tempo_restante = processos[i].burst_time;
        processos[i].tempo_espera = 0;
        processos[i].tempo_retorno = 0;
    }

    while (executado < n) {
        int i = fila[inicio++];
        if (inicio == n) inicio = 0;

        if (processos[i].tempo_restante > quantum) {
            tempo_corrente += quantum + 1; // Incluindo tempo de mudança de contexto
            processos[i].tempo_restante -= quantum;

            for (int j = inicio; j != fim; j = (j + 1) % n) {
                processos[fila[j]].tempo_espera += quantum + 1;
            }

            fila[fim++] = i;
            if (fim == n) fim = 0;
        } else {
            tempo_corrente += processos[i].tempo_restante + 1;
            for (int j = inicio; j != fim; j = (j + 1) % n) {
                processos[fila[j]].tempo_espera += processos[i].tempo_restante + 1;
            }

            processos[i].tempo_retorno = tempo_corrente;
            processos[i].tempo_restante = 0;
            executado++;
        }
    }

    free(fila);
}

Processo* gerar_processos(int n, int intervalo1[], int intervalo2[]) {
    Processo *processos = (Processo *)malloc(n * sizeof(Processo));

    for (int i = 0; i < n; i++) {
        processos[i].id = i;
        if (rand() % 2 == 0) {
            processos[i].burst_time = intervalo1[0] + rand() % (intervalo1[1] - intervalo1[0] + 1);
        } else {
            processos[i].burst_time = intervalo2[0] + rand() % (intervalo2[1] - intervalo2[0] + 1);
        }
    }

    return processos;
}

void calcular_metricas(Processo processos[], int n) {
    double tempo_medio_espera = 0, tempo_medio_retorno = 0;
    for (int i = 0; i < n; i++) {
        tempo_medio_espera += processos[i].tempo_espera;
        tempo_medio_retorno += processos[i].tempo_retorno;
    }

    tempo_medio_espera /= n;
    tempo_medio_retorno /= n;

    printf("Tempo médio de espera: %.2f\n", tempo_medio_espera);
    printf("Tempo médio de retorno: %.2f\n", tempo_medio_retorno);
}

int main() {
    int n = 5;
    int intervalo1[] = {5, 10};
    int intervalo2[] = {10, 20};

    Processo* processos = gerar_processos(n, intervalo1, intervalo2);
    int quantum = 4;
    escalonamento_round_robin(processos, n, quantum);
    calcular_metricas(processos, n);

    free(processos);
    return 0;
}
