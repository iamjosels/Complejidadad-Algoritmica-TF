class Grafo:
    def __init__(self):
        self.nodos = {}  # Diccionario para almacenar los nodos y sus atributos
    
    def agregar_nodo(self, nodo):
        if nodo not in self.nodos:
            self.nodos[nodo] = {}
    
    def agregar_arista(self, nodo_origen, nodo_destino, peso):
        if nodo_origen in self.nodos and nodo_destino in self.nodos:
            if nodo_destino not in self.nodos[nodo_origen]:
                self.nodos[nodo_origen][nodo_destino] = peso
                self.nodos[nodo_destino][nodo_origen] = peso
    
    def __str__(self):
        return str(self.nodos)
    
    def obtener_peso_aristas(self, nodo_origen, nodo_destino):
        if nodo_origen in self.nodos and nodo_destino in self.nodos[nodo_origen]:
            peso = self.nodos[nodo_origen][nodo_destino]
            return peso
        else:
            return None
        
    def imprimir_relaciones(self, nodo):
        if nodo in self.nodos:
            relaciones = self.nodos[nodo]
            for nodo_destino, peso in relaciones.items():
                print(f"Relación: {nodo} -> {nodo_destino}, Peso: {peso}")
        else:
            print(f"No se encontró el nodo: {nodo}")
    
    def obtener_pel_sig(self,pelicula_actual):
        pel_sig = []
        for nodo, vecinos in self.nodos.items():
                if(nodo==pelicula_actual):
                    for vecino in vecinos:
                        pel_sig.append(vecino)

        return pel_sig