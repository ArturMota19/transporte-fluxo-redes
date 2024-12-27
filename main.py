class TransporteFluxo:
    def __init__ (self, cidades):
        self.V = cidades # cria o número de cidades (os nós do meu grafo)
        self.grafo = [[0] * cidades for _ in range(cidades)] # cria uma matriz de adjascência para o grafo
    
    def adicionaRotas(self, origem, destino, capacidade):
        self.grafo[origem][destino] = capacidade # adiciona a capacidade c(e) na aresta (u, v)
      
    
    