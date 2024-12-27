class TransporteFluxo:
    def __init__ (self, cidades):
        self.V = cidades # cria o número de cidades (os nós do meu grafo)
        self.grafo = [[0] * cidades for _ in range(cidades)] # cria uma matriz de adjascência para o grafo
    
    def adicionaRotas(self, origem, destino, capacidade):
        self.grafo[origem][destino] = capacidade # adiciona a capacidade c(e) na aresta (u, v)
      
    def _dfs(self, origem, destino, pais):
        visitado = [False] * self.V # cria um vetor de visitados com o tamanho do número de cidades
        stack = [origem] # cria uma pilha com a origem
        visitado[origem] = True # marca a origem como visitada

        while stack: 
            u = stack.pop() # remove o último elemento da pilha

            for v in range(self.V):
                if not visitado[v] and self.grafo[u][v] > 0: # se ainda não foi visitado e a capacidade da aresta é maior que 0
                    stack.append(v) # adiciona o vértice na pilha
                    visitado[v] = True # marca o vértice como visitado
                    pais[v] = u # marca o pai do vértice como u
                    if v == destino:
                        return True
        return False 
    
    