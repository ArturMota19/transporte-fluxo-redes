class TransporteFluxo:
    def __init__ (self, cidades):
        self.V = cidades # cria o número de cidades (os nós do meu grafo)
        self.grafo = [[0] * cidades for _ in range(cidades)] # cria uma matriz de adjascência para o grafo
    
    