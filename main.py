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
      
    def calcularFluxoMaximo(self, origem, destino): # calcula o fluxo máximo de origem para destino
        pais = [-1] * self.V # cria um vetor de pais com o tamanho do número de cidades
        fluxo_maximo = 0 # inicializa o fluxo máximo como 0

        while self._dfs(origem, destino, pais): # enquanto existir um caminho de origem para destino
            fluxo_caminho = float('Inf') # inicializa o fluxo do caminho como infinito
            v = destino 
            while v != origem:
                u = pais[v] 
                fluxo_caminho = min(fluxo_caminho, self.grafo[u][v]) # o fluxo do caminho é o mínimo entre o fluxo do caminho e a capacidade da aresta
                v = pais[v] 

            v = destino
            while v != origem:
                u = pais[v]
                self.grafo[u][v] -= fluxo_caminho
                self.grafo[v][u] += fluxo_caminho
                v = pais[v]

            fluxo_maximo += fluxo_caminho # o fluxo máximo é incrementado pelo fluxo do caminho

        return fluxo_maximo

    

if __name__ == "__main__":
    #Exemplo aleatório de uso
    cidades = 6
    transporte = TransporteFluxo(cidades)

    # Adicionando rotas com capacidade
    transporte.adicionaRotas(0, 1, 100)  
    transporte.adicionaRotas(1, 2, 50)  
    transporte.adicionaRotas(2, 3, 30)  
    transporte.adicionaRotas(3, 4, 20) 
    transporte.adicionaRotas(4, 5, 10) 
    
    origem = 0 
    destino = 4

    print(f"Fluxo máximo da origem ao destino: {transporte.calcularFluxoMaximo(origem, destino)}")