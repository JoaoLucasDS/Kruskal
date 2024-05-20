import operator
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Vertice(object):
    def __init__(self, tag):
        self.tag = tag
        self.cor = None
        self.descoberta = None
        self.antecessor = None
        self.Final = None
        self.listaAdj = []

    def buscaAdj(self, vert):
        if vert in self.listaAdj:
            return True
        return False

class Aresta(object):
    def __init__(self, VerticeEntr: Vertice, VerticeSaid: Vertice, peso):
        self.tag = VerticeEntr.tag + " - " + VerticeSaid.tag
        self.VerticeEntr = VerticeEntr
        self.VerticeSaid = VerticeSaid
        self.peso = peso

class Grafo(object):
    def __init__(self, direcionado):
        self.listaVertices = []
        self.listaArestas = []
        self.direcionado = direcionado
        self.matriz = []
        self.OrdTopologica = []
        self.tempo = 0

    # Vertices
    def verificaVertice(self, vert):
        if isinstance(vert, Vertice):
            return True
        return False

    def buscaVertice(self, vert):
        if self.verificaVertice(vert):
            if vert in self.listaVertices:
                return True
        return False

    def addVert(self, vert):
        if self.buscaVertice(vert):
            print("Vertice já existe no Grafo")
        else:
            if self.verificaVertice(vert):
                self.listaVertices.append(vert)
                print("Vertice", vert.tag, "adicionado com sucesso.")
            else:
                print("Erro: Espera-se um Vertice")

    # Arestas
    def verificaAresta(self, arest):
        if isinstance(arest, Aresta):
            if self.buscaVertice(arest.VerticeEntr) and self.buscaVertice(arest.VerticeSaid):
                return True
        return False

    def buscaAresta(self, arest):
        if self.verificaVertice(arest):
            if arest in self.listaVertices:
                return True
        return False

    def buscaAresta2(self, arest):
        if self.verificaAresta(arest):
            for i in self.listaArestas:
                if (arest.VerticeEntr.tag == i.VerticeEntr.tag) and (arest.VerticeSaid.tag == i.VerticeSaid.tag):
                    return True
        return False

    def addAresta(self, arest):
        if self.buscaAresta2(arest):
            print("Aresta já existe no Grafo")
        else:
            if self.verificaAresta(arest):
                self.listaArestas.append(arest)
                print("Aresta", arest.tag, "Adicionada com sucesso")
                self.addAdj(arest.VerticeEntr)
                self.addAdj(arest.VerticeSaid)
                if not self.direcionado:
                    self._duplica(arest)
            else:
                print("Erro: Espera-se uma Aresta valida")

    def _duplica(self, arest):
        arestRev = Aresta(arest.VerticeSaid, arest.VerticeEntr, arest.peso)
        self.addAresta(arestRev)

    # operações
    def addAdj(self, vert):
        if self.buscaVertice(vert):
            for i in self.listaArestas:
                if vert.tag == i.VerticeEntr.tag and not vert.buscaAdj(i.VerticeSaid):
                    vert.listaAdj.append(i.VerticeSaid)
        else:
            print("Erro: Espera-se um Vertice")

    vertID = {}

    # Kruskal
    def find(self, vert):
        for i, j in self.vertID.items():
            if vert in j:
                return i
        return None

    def makeSet(self, vert):
        self.vertID[vert] = set([vert])

    def uni(self, x, y):
        vertX = self.find(x)
        vertY = self.find(y)
        self.vertID[vertX] = self.vertID[vertY].union(self.vertID[vertX])
        del self.vertID[vertY]

    def Kruskal(self):
        A = []
        for vert in self.listaVertices:
            self.makeSet(vert)
        ArestasOrd = self.listaArestas
        ArestasOrd.sort(key=operator.attrgetter('peso'))
        for aresta in ArestasOrd:
            if self.find(aresta.VerticeEntr) != self.find(aresta.VerticeSaid):
                A.append(aresta.tag)
                self.uni(aresta.VerticeEntr, aresta.VerticeSaid)
        return A

    def KruskalAnimado(self):
        A = []
        G = nx.Graph()

        pos = {}
        for vert in self.listaVertices:
            pos[vert.tag] = (hash(vert.tag) % 100, hash(vert.tag) // 100)

        for vert in self.listaVertices:
            self.makeSet(vert)
            G.add_node(vert.tag)

        ArestasOrd = self.listaArestas
        ArestasOrd.sort(key=operator.attrgetter('peso'))

        fig, ax = plt.subplots()
        nx.draw(G, pos, ax=ax, with_labels=True)

        def update(frame):
            aresta = ArestasOrd[frame]
            if self.find(aresta.VerticeEntr) != self.find(aresta.VerticeSaid):
                A.append(aresta.tag)
                self.uni(aresta.VerticeEntr, aresta.VerticeSaid)
                G.add_edge(aresta.VerticeEntr.tag, aresta.VerticeSaid.tag, weight=aresta.peso)
                ax.clear()
                nx.draw(G, pos, ax=ax, with_labels=True, edge_color='black')
                labels = nx.get_edge_attributes(G, 'weight')
                nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
            return ax

        anim = FuncAnimation(fig, update, frames=range(len(ArestasOrd)), repeat=False)
        plt.show()
        return A

    # Print
    def contador(self):
        if self.direcionado == True:
            print("Número de Vertices:", int(len(self.listaVertices)), ", Número de Arestas: ", int(len(self.listaArestas)))
        else:
            print("Número de Vertices:", int(len(self.listaVertices)), ", Número de Arestas: ", int(len(self.listaArestas) / 2))

    def mostraGrafo(self):
        print("*" * 8, "Grafo", "*" * 8)
        print("Vertices:")
        for i in self.listaVertices:
            print("|", i.tag, end=" ", )
        print("|")
        print("Arestas:")
        for j in self.listaArestas:
            if not self.direcionado:
                if self.listaArestas.index(j) % 2 == 0:
                    print(j.tag)
            else:
                print(j.tag)

    def mostraListaAdj(self, vert):
        repreLista = []
        for i in vert.listaAdj:
            repreLista.append(i.tag)
        print(vert.tag, "->", repreLista)
