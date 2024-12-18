Aqui está um exemplo de um arquivo `README.md` adequado para o seu projeto "Sistemas Operacionais - Trabalho 1", com base nos detalhes fornecidos:

```markdown
# Sistemas Operacionais - Trabalho 1

## Descrição

Este repositório contém o código e a documentação para o Trabalho 1 da disciplina de **Sistemas Operacionais**, lecionada pelo Prof. Daniel Ferreira no **IFCE - Campus Maracanaú**. O trabalho é composto por três questões que envolvem a implementação e simulação de algoritmos de escalonamento e resolução de problemas clássicos de concorrência. As questões são:

1. **Simulação do algoritmo de escalonamento Round Robin.**
2. **Protocolo de solução do problema do jantar dos filósofos sem impasse.**
3. **Simulação para comparar duas soluções para o problema dos leitores e escritores.**

## Objetivo

O objetivo deste trabalho é desenvolver simulações para analisar algoritmos e protocolos de escalonamento e sincronização em sistemas operacionais. Para cada questão, foram realizados experimentos e os resultados foram apresentados em gráficos e análises.

## Estrutura do Repositório

O repositório está organizado da seguinte maneira:

- **questao1/**: Implementação e gráficos do algoritmo de escalonamento Round Robin.
  - `gerar_graficos_round_robin.py`: Código Python para gerar os gráficos de tempo médio de espera e retorno.
  - `round_robin.c`: Código em C para a simulação do algoritmo Round Robin.
  - `tempo_medio_espera.png`: Gráfico com o tempo médio de espera para diferentes valores de quantum.
  - `tempo_medio_retorno.png`: Gráfico com o tempo médio de retorno para diferentes valores de quantum.

- **questao2/**: Implementação e gráficos relacionados ao problema do jantar dos filósofos.
  - `gerar_graficos_impasses.py`: Código Python para gerar os gráficos de impasses no jantar dos filósofos.
  - `grafico_impasses.png`: Gráfico com a quantidade de impasses em 1000 execuções.
  - `Jantar dos Filósofos.pdf`: Documento com a explicação detalhada do protocolo implementado.
  - `jantar_filosofos.c`: Código em C para a simulação do problema do jantar dos filósofos.

- **questao3/**: Implementação e gráficos do problema dos leitores e escritores.
  - `comparacao_solucoes.png`: Gráfico comparando as duas soluções para o problema dos leitores e escritores.
  - `gerar_graficos_leitores_escritores.py`: Código Python para gerar os gráficos de comparação entre as soluções.
  - `Leitores e Escritores.pdf`: Documento com a descrição das soluções implementadas.
  - `leitores_escritores_solucao1.c`: Código em C com a primeira solução para o problema dos leitores e escritores.
  - `leitores_escritores_solucao2.c`: Código em C com a segunda solução para o problema dos leitores e escritores.

## Como Executar

### Questão 1: Round Robin
Para executar a simulação do algoritmo de escalonamento Round Robin, compile o código `round_robin.c` e rode o programa. Utilize o script Python `gerar_graficos_round_robin.py` para gerar os gráficos de tempo médio de espera e retorno.

```bash
gcc round_robin.c -o round_robin
./round_robin
python gerar_graficos_round_robin.py
```

### Questão 2: Jantar dos Filósofos
O código em C `jantar_filosofos.c` implementa o protocolo para o problema do jantar dos filósofos. O script Python `gerar_graficos_impasses.py` gera os gráficos que mostram o número de impasses ocorridos em 1000 execuções.

```bash
gcc jantar_filosofos.c -o jantar_filosofos
./jantar_filosofos
python gerar_graficos_impasses.py
```

### Questão 3: Leitores e Escritores
As duas soluções para o problema dos leitores e escritores estão implementadas nos arquivos `leitores_escritores_solucao1.c` e `leitores_escritores_solucao2.c`. O script Python `gerar_graficos_leitores_escritores.py` gera os gráficos comparativos.

```bash
gcc leitores_escritores_solucao1.c -o solucao1
gcc leitores_escritores_solucao2.c -o solucao2
./solucao1
./solucao2
python gerar_graficos_leitores_escritores.py
```

## Relatório

O relatório completo do trabalho está disponível no **arquivo PDF** e contém as descrições detalhadas dos experimentos, métodos utilizados e resultados obtidos.

## Tecnologias Utilizadas

- **C**: Para a implementação dos algoritmos de escalonamento e protocolos de sincronização.
- **Python**: Para a geração de gráficos e análise de resultados.
- **GNU Compiler Collection (GCC)**: Para compilar os códigos em C.
- **Matplotlib**: Para a criação de gráficos em Python.

## Conclusão

O trabalho proporciona uma visão prática sobre algoritmos de escalonamento e protocolos de sincronização em sistemas operacionais, contribuindo para a compreensão dos conceitos fundamentais de concorrência e escalonamento em sistemas multitarefa.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).
```

Esse `README.md` contém uma descrição clara do projeto, estrutura dos arquivos, como executar o código e informações sobre as tecnologias utilizadas.