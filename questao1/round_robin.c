#include <stdio.h>
#include <stdlib.h>
#include <math.h>

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

    // Inicialização dos processos
    for (int i = 0; i < n; i++) {
        fila[fim++] = i;
        processos[i].tempo_restante = processos[i].burst_time;
        processos[i].tempo_espera = 0;
        processos[i].tempo_retorno = 0;
    }

    // Algoritmo Round Robin
    while (executado < n) {
        int i = fila[inicio++];
        if (inicio == n) inicio = 0;
        
        if (processos[i].tempo_restante > quantum) {
            tempo_corrente += quantum + 1;  // Incluindo tempo de mudança de contexto
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

void calcular_metricas(Processo processos[], int n, FILE *saida) {
    double tempo_medio_espera = 0.0;
    double tempo_medio_retorno = 0.0;
    double desvio_espera = 0.0;
    double desvio_retorno = 0.0;

    // Cálculo do tempo médio de espera e tempo médio de retorno
    for (int i = 0; i < n; i++) {
        tempo_medio_espera += processos[i].tempo_espera;
        tempo_medio_retorno += processos[i].tempo_retorno;
    }
    
    tempo_medio_espera /= n;
    tempo_medio_retorno /= n;

    // Cálculo do desvio padrão para tempo de espera
    for (int i = 0; i < n; i++) {
        desvio_espera += pow(processos[i].tempo_espera - tempo_medio_espera, 2);
        desvio_retorno += pow(processos[i].tempo_retorno - tempo_medio_retorno, 2);
    }

    desvio_espera = sqrt(desvio_espera / n);
    desvio_retorno = sqrt(desvio_retorno / n);

    // Impressão dos resultados no arquivo
    fprintf(saida, "%d %.2f %.2f %.2f %.2f\n", n, tempo_medio_espera, desvio_espera, tempo_medio_retorno, desvio_retorno);
}

int main() {
    int n = 5;  // Número de processos
    int intervalo1[] = {10, 20};  // Intervalo para burst_time 1
    int intervalo2[] = {30, 40};  // Intervalo para burst_time 2
    int quantum[] = {1, 2, 4, 8}; // Quantums a testar

    FILE *saida = fopen("resultados.txt", "w");

    if (!saida) {
        printf("Erro ao abrir arquivo de saída.\n");
        return 1;
    }

    // Gerar os processos
    Processo *processos = gerar_processos(n, intervalo1, intervalo2);

    for (int i = 0; i < 4; i++) {
        printf("Executando Round Robin com quantum = %d\n", quantum[i]);
        escalonamento_round_robin(processos, n, quantum[i]);
        calcular_metricas(processos, n, saida);
    }

    fclose(saida);
    free(processos);

    printf("Resultados salvos em 'resultados.txt'.\n");
    return 0;
}
