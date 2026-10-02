from collections import deque


# === К1: Класс DirectedGraph ===
class DirectedGraph:
    """Ориентированный граф на основе словаря."""

    def __init__(self):
        self.adjacency = {}

    def add_vertex(self, vertex):
        """Добавить вершину."""
        if vertex not in self.adjacency:
            self.adjacency[vertex] = []

    def add_edge(self, from_v, to_v):
        """Добавить ребро from_v → to_v."""
        self.add_vertex(from_v)
        self.add_vertex(to_v)
        self.adjacency[from_v].append(to_v)

    def __str__(self):
        lines = ["DirectedGraph:"]
        for v, neighbors in self.adjacency.items():
            lines.append(f"  {v} → {neighbors}")
        return "\n".join(lines)


# === К2: BFS для ориентированного графа ===
def bfs(graph, start):
    """Обход в ширину. Возвращает порядок посещения."""
    visited = set()
    order = []
    queue = deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        for neighbor in graph.adjacency.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order


# === К3: Матрица смежности из списка рёбер ===
def create_adjacency_matrix(edges, vertices=None):
    """Создаёт матрицу смежности из списка рёбер."""
    if vertices is None:
        vertices = sorted(set([v for edge in edges for v in edge]))

    index = {v: i for i, v in enumerate(vertices)}
    n = len(vertices)
    matrix = [[0] * n for _ in range(n)]

    for u, v in edges:
        matrix[index[u]][index[v]] = 1
    return matrix, vertices


def add_vertex_matrix(matrix, vertices, vertex):
    """Добавить вершину в матрицу смежности."""
    if vertex in vertices:
        return matrix, vertices
    n = len(vertices)
    new_matrix = [row + [0] for row in matrix]
    new_matrix.append([0] * (n + 1))
    vertices.append(vertex)
    return new_matrix, vertices


def add_edge_matrix(matrix, vertices, from_v, to_v):
    """Добавить ребро в матрицу смежности."""
    if from_v not in vertices:
        matrix, vertices = add_vertex_matrix(matrix, vertices, from_v)
    if to_v not in vertices:
        matrix, vertices = add_vertex_matrix(matrix, vertices, to_v)
    i, j = vertices.index(from_v), vertices.index(to_v)
    matrix[i][j] = 1
    return matrix, vertices


def print_matrix(matrix, vertices):
    """Печать матрицы смежности."""
    print("    " + " ".join(f"{v:>3}" for v in vertices))
    for i, v in enumerate(vertices):
        print(f"{v:>3} " + " ".join(f"{x:>3}" for x in matrix[i]))


# === К4: Список смежности из списка рёбер ===
def create_adjacency_list(edges):
    """Создаёт список смежности из списка рёбер."""
    adj_list = {}
    for u, v in edges:
        adj_list.setdefault(u, []).append(v)
        adj_list.setdefault(v, [])
    return adj_list


def add_vertex_list(adj_list, vertex):
    """Добавить вершину в список смежности."""
    if vertex not in adj_list:
        adj_list[vertex] = []
    return adj_list


def add_edge_list(adj_list, from_v, to_v):
    """Добавить ребро в список смежности."""
    adj_list = add_vertex_list(adj_list, from_v)
    adj_list = add_vertex_list(adj_list, to_v)
    adj_list[from_v].append(to_v)
    return adj_list


def print_adjacency_list(adj_list):
    """Печать списка смежности."""
    for v, neighbors in adj_list.items():
        print(f"  {v} → {neighbors}")


# === Проверка ===
if __name__ == "__main__":
    print("=== К1: DirectedGraph ===")
    g = DirectedGraph()
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("C", "D")
    g.add_edge("D", "E")
    print(g)

    print("\n=== К2: BFS ===")
    print(f"BFS от A: {bfs(g, 'A')}")
    print(f"BFS от B: {bfs(g, 'B')}")

    print("\n=== К3: Матрица смежности ===")
    edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")]
    matrix, vertices = create_adjacency_matrix(edges)
    print(f"Вершины: {vertices}")
    print_matrix(matrix, vertices)

    # Добавление вершины и ребра
    matrix, vertices = add_vertex_matrix(matrix, vertices, "F")
    matrix, vertices = add_edge_matrix(matrix, vertices, "E", "F")
    print("\nПосле добавления F и ребра E→F:")
    print_matrix(matrix, vertices)

    print("\n=== К4: Список смежности ===")
    adj_list = create_adjacency_list(edges)
    print_adjacency_list(adj_list)

    # Добавление вершины и ребра
    adj_list = add_edge_list(adj_list, "E", "F")
    print("\nПосле добавления F и ребра E→F:")
    print_adjacency_list(adj_list)