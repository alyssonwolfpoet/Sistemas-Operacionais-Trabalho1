#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

#define NUM_FILOSOFOS 5
#define NUM_ITERACOES 1000

sem_t garfos[NUM_FILOSOFOS];
pthread_t filosofos[NUM_FILOSOFOS];

void *filosofo(void *num) {
    int id = *((int *) num);
    for (int i = 0; i < NUM_ITERACOES; i++) {
        printf("Filósofo %d está pensando.\n", id);
        usleep(rand() % 1000);
        sem_wait(&garfos[id]);
        sem_wait(&garfos[(id + 1) % NUM_FILOSOFOS]);
        printf("Filósofo %d está comendo.\n", id);
        usleep(rand() % 1000);
        sem_post(&garfos[id]);
        sem_post(&garfos[(id + 1) % NUM_FILOSOFOS]);
    }
    pthread_exit(NULL);
}

int main() {
    int ids[NUM_FILOSOFOS];
    for (int i = 0; i < NUM_FILOSOFOS; i++) {
        sem_init(&garfos[i], 0, 1);
    }

    for (int i = 0; i < NUM_FILOSOFOS; i++) {
        ids[i] = i;
        pthread_create(&filosofos[i], NULL, filosofo, &ids[i]);
    }

    for (int i = 0; i < NUM_FILOSOFOS; i++) {
        pthread_join(filosofos[i], NULL);
    }

    for (int i = 0; i < NUM_FILOSOFOS; i++) {
        sem_destroy(&garfos[i]);
    }

    return 0;
}
