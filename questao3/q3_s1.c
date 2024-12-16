#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

sem_t mutex, wrt;
int leitores = 0;

void *leitor(void *num) {
    int id = *((int *) num);
    
    while (1) {
        sem_wait(&mutex);
        leitores++;
        if (leitores == 1)
            sem_wait(&wrt);
        sem_post(&mutex);
        
        printf("Leitor %d está lendo\n", id);
        usleep(rand() % 1000);
        
        sem_wait(&mutex);
        leitores--;
        if (leitores == 0)
            sem_post(&wrt);
        sem_post(&mutex);
        
        usleep(rand() % 1000);
    }
}

void *escritor(void *num) {
    int id = *((int *) num);
    
    while (1) {
        sem_wait(&wrt);
        
        printf("Escritor %d está escrevendo\n", id);
        usleep(rand() % 1000);
        
        sem_post(&wrt);
        usleep(rand() % 1000);
    }
}

int main() {
    pthread_t read[5], write[5];
    int ids[5];
    
    sem_init(&mutex, 0, 1);
    sem_init(&wrt, 0, 1);
    
    for (int i = 0; i < 5; i++) {
        ids[i] = i;
        pthread_create(&read[i], NULL, leitor, &ids[i]);
        pthread_create(&write[i], NULL, escritor, &ids[i]);
    }
    
    for (int i = 0; i < 5; i++) {
        pthread_join(read[i], NULL);
        pthread_join(write[i], NULL);
    }
    
    sem_destroy(&mutex);
    sem_destroy(&wrt);
    
    return 0;
}
