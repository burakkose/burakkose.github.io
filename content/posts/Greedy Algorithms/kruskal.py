parent = dict()
rank = dict()


def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0


def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]


def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1


def get_sorted_edges(graph):
    'Kenarları elde edelim'
    edges = []
    for src in graph:
        for dest in graph[src]:
            edges.append(tuple(src) + dest)
    return sorted(edges, key=lambda x: x[2])


def print_kruskal(graph):
    for vertex in graph:
        make_set(vertex)
    sorted_edges = get_sorted_edges(graph)
    for edge in sorted_edges:
        v1, v2, w = edge
        if find(v1) != find(v2):
            union(v1, v2)
            print(edge)  # sonuc

if __name__ == '__main__':
    """
            10
        0--------1
        |  \     |
       6|   5\   |15
        |      \ |
        2--------3
            4
    Vertices = 0,1,2,3
    """
    graph = {"0": [("1", 10), ("2", 6), ("3", 5)],
             "1": [("3", 15)],
             "2": [("3", 4)],
             "3": []}
    print_kruskal(graph)
