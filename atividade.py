from collections import deque
import heapq


DIRECOES = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # cima, direita, baixo, esquerda[cite: 8]

def achar(lab, simbolo):
    for i, linha in enumerate(lab):
        if simbolo in linha:
            return (i, linha.index(simbolo)) #[cite: 7]

def livre(lab, i, j):
    dentro = 0 <= i < len(lab) and 0 <= j < len(lab[0])
    return dentro and lab[i][j] != '#' #[cite: 8]

def montar_grafo(lab):
    grafo = {}
    for i in range(len(lab)):
        for j in range(len(lab[0])):
            if not livre(lab, i, j):
                continue
            grafo[(i, j)] = []
            for di, dj in DIRECOES:
                if livre(lab, i + di, j + dj):
                    grafo[(i, j)].append((i + di, j + dj))
    return grafo #[cite: 8]

def desenhar(lab, caminho):
    grade = [list(linha) for linha in lab]
    for i, j in caminho:
        if grade[i][j] == '.':
            grade[i][j] = '*'
    for linha in grade:
        print(''.join(linha)) 


labirinto = [
    "I........#",
    ".#######.#",
    ".......#.#",
    "######.#.#",
    ".....#.#.#",
    "####.#.#.#",
    "...#.#.#.#",
    "##.#.#.#.#",
    ".......#..",
    "######...F"
]

inicio = achar(labirinto, 'I')
saida = achar(labirinto, 'F')
grafo = montar_grafo(labirinto)


def reconstruir_caminho(pai, atual):
    caminho = [atual]
    while atual in pai:
        atual = pai[atual]
        caminho.append(atual)
    caminho.reverse()
    return caminho

def dfs(grafo, inicio, saida):
    visitados = set()
    pilha = [inicio]
    pai = {}
    
    while pilha:
        v = pilha.pop() 
        if v in visitados:
            continue
            
        visitados.add(v)
        
        if v == saida:
            return reconstruir_caminho(pai, v), len(visitados)
            
        
        for w in reversed(grafo[v]):
            if w not in visitados:
                pai[w] = v
                pilha.append(w)
                
    return [], len(visitados)

def bfs(grafo, inicio, saida):
    visitados = {inicio}
    fila = deque([inicio]) 
    pai = {}
    
    while fila:
        v = fila.popleft()
        
        if v == saida:
            return reconstruir_caminho(pai, v), len(visitados)
            
        for w in grafo[v]:
            if w not in visitados:
                visitados.add(w)
                pai[w] = v
                fila.append(w)
                
    return [], len(visitados)

def busca_gulosa(grafo, inicio, saida):
    def h(v, saida):
        
        return abs(v[0] - saida[0]) + abs(v[1] - saida[1])
        
    visitados = set()
    fronteira = [(h(inicio, saida), inicio)] 
    pai = {}
    
    while fronteira:
        _, v = heapq.heappop(fronteira)
        
        if v in visitados:
            continue
            
        visitados.add(v)
        
        if v == saida:
            return reconstruir_caminho(pai, v), len(visitados)
            
        for w in grafo[v]:
            if w not in visitados:
                
                if w not in pai: 
                    pai[w] = v
                heapq.heappush(fronteira, (h(w, saida), w))
                
    return [], len(visitados)



print("=== DFS ===")
cam_dfs, vis_dfs = dfs(grafo, inicio, saida)
desenhar(labirinto, cam_dfs)
print(f"Tamanho do caminho: {len(cam_dfs)} | Casas visitadas: {vis_dfs}\n")

print("=== BFS ===")
cam_bfs, vis_bfs = bfs(grafo, inicio, saida)
desenhar(labirinto, cam_bfs)
print(f"Tamanho do caminho: {len(cam_bfs)} | Casas visitadas: {vis_bfs}\n")

print("=== BUSCA GULOSA ===")
cam_gul, vis_gul = busca_gulosa(grafo, inicio, saida)
desenhar(labirinto, cam_gul)
print(f"Tamanho do caminho: {len(cam_gul)} | Casas visitadas: {vis_gul}\n")