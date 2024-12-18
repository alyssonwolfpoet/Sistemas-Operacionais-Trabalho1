A estrutura do seu projeto está bem organizada! Vou sugerir algumas melhorias no seu arquivo `README.md` com base na estrutura de diretórios e arquivos que você forneceu. Abaixo está o `README.md` ajustado, com os detalhes da estrutura do projeto:

---

# Trabalho de Sistemas Operacionais - Algoritmos e Simulações

Este repositório contém as implementações para o trabalho da disciplina **Sistemas Operacionais** do curso **IFCE - Campus Maracanaú**, sob orientação do Prof. Daniel Ferreira. O trabalho aborda a simulação de algoritmos de escalonamento, criação de protocolos e resolução de problemas clássicos de sincronização.

## Objetivo

O objetivo deste projeto é implementar e simular os seguintes tópicos:

1. **Simulação do algoritmo de escalonamento Round Robin**
2. **Criação de um protocolo para o problema do jantar dos filósofos sem impasse**
3. **Simulação do problema dos leitores e escritores para comparar soluções**

Essas implementações são feitas em **C**, com a geração de gráficos para análise dos resultados em **Python**.

## Estrutura do Repositório

O projeto está organizado da seguinte forma:

```
Sistemas-Operacionais-Trabalho1/
├── .gitignore                 # Arquivo para ignorar arquivos temporários
├── Código.pdf                 # Código-fonte detalhado ou outro material complementar
├── README.md                  # Este arquivo de documentação
├── requirements.txt           # Dependências necessárias para gerar gráficos
├── resultados.png             # Imagem com os resultados gerais
├── questao1/
│   ├── gerar_graficos_round_robin.py  # Script Python para gerar gráficos de Round Robin
│   ├── round_robin.c                 # Implementação do algoritmo Round Robin
│   ├── tempo_medio_espera.png        # Gráfico do tempo médio de espera
│   ├── tempo_medio_retorno.png       # Gráfico do tempo médio de retorno
│   └── output/                        # Diretório para armazenar arquivos de saída
├── questao2/
│   ├── gerar_graficos_impasses.py    # Script Python para gerar gráficos dos impasses
│   ├── grafico_impasses.png          # Gráfico mostrando impasses no jantar dos filósofos
│   ├── Jantar dos Filósofos.pdf      # Documento explicativo sobre o jantar dos filósofos
│   ├── jantar_filosofos.c            # Implementação do problema do jantar dos filósofos
│   └── output/                       # Diretório para armazenar arquivos de saída
├── questao3/
│   ├── comparacao_solucoes.png       # Gráfico comparando soluções para leitores e escritores
│   ├── gerar_graficos_leitores_escritores.py  # Script Python para gerar gráficos de leitores e escritores
│   ├── leitores_escritores_solucao1.c  # Implementação da solução 1 do problema leitores e escritores
│   ├── leitores_escritores_solucao2.c  # Implementação da solução 2 do problema leitores e escritores
│   └── output/                       # Diretório para armazenar arquivos de saída
```

## Dependências

Certifique-se de ter as dependências necessárias instaladas. Use o arquivo `requirements.txt` para instalar as bibliotecas Python necessárias:

```bash
pip install -r requirements.txt
```

As bibliotecas necessárias são:

- `matplotlib`
- `seaborn`

## Compilação

Para compilar e rodar as simulações, siga os seguintes passos:

### Requisitos

- **GCC** (Compilador C)
- **Python** (para geração dos gráficos)

### Passos para Compilação

1. **Compilar a questão 1 (Round Robin)**:

   Navegue até a pasta `questao1` e compile o arquivo `round_robin.c`:

   ```bash
   gcc -Wall -Wextra -g3 round_robin.c -o output/round_robin.exe -mconsole
   ```

2. **Compilar a questão 2 (Jantar dos Filósofos)**:

   Navegue até a pasta `questao2` e compile o arquivo `jantar_filosofos.c`:

   ```bash
   gcc -Wall -Wextra -g3 jantar_filosofos.c -o output/jantar_filosofos.exe -mconsole
   ```

3. **Compilar a questão 3 (Leitores e Escritores)**:

   Navegue até a pasta `questao3` e compile o arquivo `leitores_escritores_solucao1.c` ou `leitores_escritores_solucao2.c`:

   ```bash
   gcc -Wall -Wextra -g3 leitores_escritores_solucao1.c -o output/leitores_escritores_solucao1.exe -mconsole
   gcc -Wall -Wextra -g3 leitores_escritores_solucao2.c -o output/leitores_escritores_solucao2.exe -mconsole
   ```

### Geração de Gráficos

Após rodar as simulações e gerar os resultados em arquivos de saída, você pode utilizar os scripts Python para gerar gráficos a partir desses dados. 

Para gerar os gráficos de **Round Robin**:

```bash
python gerar_graficos_round_robin.py
```

Para gerar os gráficos de **Jantar dos Filósofos**:

```bash
python gerar_graficos_impasses.py
```

Para gerar os gráficos de **Leitores e Escritores**:

```bash
python gerar_graficos_leitores_escritores.py
```

## Execução

1. Execute o arquivo executável da questão desejada:

   ```bash
   ./output/round_robin.exe
   ./output/jantar_filosofos.exe
   ./output/leitores_escritores_solucao1.exe
   ./output/leitores_escritores_solucao2.exe
   ```

2. Após a execução, os gráficos serão gerados automaticamente pelos scripts Python.

## Relatório

O trabalho inclui um relatório final, disponível no diretório `questao2/`, onde são discutidos os resultados das simulações e comparadas as soluções encontradas para os problemas de sincronização.

---

Este arquivo `README.md` deve oferecer uma visão geral clara sobre como organizar, compilar e gerar gráficos a partir dos resultados. Se precisar de mais algum detalhe, estarei à disposição!