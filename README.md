# Atividade 9 - Algoritmos de Busca em Labirinto
Disciplina: Algoritmos e Estruturas de Dados II  
Professor: Pablo De Chiaro  

# Labirinto
Foi criado um labirinto de dimensão 10x10 usando as marcações padrão (`I` para início, `F` para fim, `#` para parede e `.` para caminho livre). 

O labirinto possui duas rotas até a saída:
1- Uma rota principal pela parte superior e direita (mais longa).
2- Uma rota pela parte inferior (mais curta).

Também foram colocados alguns becos sem saída para testar o comportamento dos algoritmos ao precisarem fazer backtracking.


# Implementação

Para a resolução do problema, foram mantidas as funções fornecidas em aula (`achar`, `livre`, `montar_grafo` e `desenhar`). Os algoritmos foram adaptados para retornar uma tupla contendo `(caminho, casas_visitadas)`:

- DFS (Busca em Profundidade): Utiliza estrutura de pilha. Explora cada ramo até o limite antes de voltar.
- BFS (Busca em Largura): Utiliza fila (`deque`). Explora o grafo em camadas a partir da origem.
- Gulosa (Greedy Best-First Search): Utiliza fila de prioridade (`heapq`) com a distância de Manhattan como função heurística $h(v)$.

 Para reconstruir o caminho percorrido do início ao fim, foi utilizado um dicionário de mapeamento `pai[vizinho] = atual`. Ao encontrar a saída `F`, o algoritmo recupera o trajeto voltando do fim para o início e inverte a lista.

---

# Resultados Obtidos

| Algoritmo | Tamanho do Caminho | Casas Visitadas |
| :--- | :---: | :---: |
| **DFS** | 46 | 53 |
| **BFS** | 18 | 39 |
| **Gulosa** | 20 | 27 |

