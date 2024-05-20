# Kruskal's Algorithm Visualization

Este projeto implementa o algoritmo de Kruskal para encontrar a árvore geradora mínima de um grafo. Além disso, utiliza as bibliotecas `matplotlib` e `networkx` para criar uma animação mostrando o processo de construção da árvore geradora mínima.

## Estrutura do Projeto

O projeto é composto pelos seguintes arquivos:

1. **kruskal.py**: Contém a implementação das classes `Vertice`, `Aresta` e `Grafo`, além dos métodos necessários para executar o algoritmo de Kruskal e gerar a animação.
2. **main.py**: Script principal que cria o grafo, adiciona vértices e arestas, e executa a animação do algoritmo de Kruskal.

## Requisitos

Certifique-se de ter Python instalado em seu ambiente. As bibliotecas necessárias podem ser instaladas usando `pip`:

```bash
pip install matplotlib networkx
```
## Uso

### Executando o Projeto

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/JoaoLucasDS/Kruskal
   cd kruskal-visualization
   ```

2. **Execute o script principal**:

   ```bash
   python main.py
   ```

Ao executar `main.py`, uma janela será aberta mostrando a animação do grafo sendo formado conforme o algoritmo de Kruskal é executado.

### Modificando o Grafo

Para adicionar ou modificar os vértices e arestas, edite o arquivo `main.py`:

- **Adicionando Vértices**:
  ```python
  vA = Vertice("a")
  g.addVert(vA)
  ```

- **Adicionando Arestas**:
  ```python
  a0 = Aresta(vA, vB, 4)
  g.addAresta(a0)
  ```

### Estrutura das Classes

- **Classe `Vertice`**:
  - `tag`: Identificador do vértice.
  - `listaAdj`: Lista de adjacência.

- **Classe `Aresta`**:
  - `VerticeEntr`: Vértice de entrada.
  - `VerticeSaid`: Vértice de saída.
  - `peso`: Peso da aresta.

- **Classe `Grafo`**:
  - `listaVertices`: Lista de vértices do grafo.
  - `listaArestas`: Lista de arestas do grafo.
  - Métodos para adicionar vértices (`addVert`) e arestas (`addAresta`), verificar a presença de vértices e arestas, e executar o algoritmo de Kruskal (`Kruskal` e `KruskalAnimado`).

### Métodos Principais

- **Kruskal**: Executa o algoritmo de Kruskal e retorna a árvore geradora mínima.
- **KruskalAnimado**: Executa o algoritmo de Kruskal com animação utilizando `matplotlib` e `networkx`.

## Contribuição

Se você deseja contribuir com este projeto, sinta-se à vontade para abrir issues ou enviar pull requests.
