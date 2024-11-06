#laberinto
import networkx as nx
import matplotlib.pyplot as plt #para dibujar el grafo

class Laberinto: 
    def __init__(self, grafo, inicio, salida):#definir laberinto
        self.grafo = grafo
        self.inicio = inicio
        self.salida = salida
        self.camino = [inicio]

    def explorar_interactivo(self): #definimos como explora el laberinto
        nodo_actual = self.inicio
        
        while nodo_actual != self.salida:
            vecinos = self.grafo.get(nodo_actual, [])
            if not vecinos:
                print("No hay salida desde este nodo. Intenta otra ruta.")
                return False

            print(f"Estás en el nodo {nodo_actual}. Opciones: {vecinos}")
            siguiente_nodo = input("Elige tu próximo nodo: ")
            
            if siguiente_nodo in vecinos:
                self.camino.append(siguiente_nodo)
                nodo_actual = siguiente_nodo
            else:
                print("Movimiento no válido. Intenta otra vez.")

        print(f"¡Has llegado a la salida! Camino seguido: {self.camino}")
        return True

    def mostrar_grafo(self):
        G = nx.DiGraph(self.grafo)
        
        pos = nx.spring_layout(G)
        plt.figure(figsize=(10, 7))
        nx.draw(G, pos, with_labels=True, node_color="skyblue", font_weight="bold", node_size=2000, font_size=12, edge_color="gray")
        plt.show()

# Representación del laberinto como un grafo
grafo = {
    'entrada': ['pantano', 'iglesia'],
    'pantano': ['entrada', 'catedral', 'cielo'],
    'iglesia': ['entrada', 'floristeria'],
    'catedral': ['pantano'],
    'cielo': ['pantano', 'floristeria', 'basurero'],
    'floristeria': ['iglesia', 'cielo', 'infierno'],
    'basurero': ['cielo'],
    'infierno': ['floristeria']
}

# Configuración del laberinto
inicio = 'entrada'
salida = 'infierno'

laberinto = Laberinto(grafo, inicio, salida)
laberinto.mostrar_grafo()

# Explorar el laberinto de forma interactiva
exito = laberinto.explorar_interactivo()
if not exito:
    print("No encontraste la salida y te ha matado netanyahhù.")
