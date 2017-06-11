Title: Kruskal Algoritması - Greedy Yaklaşımı
Date: 2015-10-11 18:00
Author: Burak
Category: Algoritma
Tags: algorithm, greedy, graph theory
Slug: kuruskal-mst

En küçük yol ağacı problemine(minimum spanning tree) üretilmiş bir çözümdür. En basit graf algoritmalarından biridir. Greedy yaklaşımı ile çözüme ulaşılır. Amaç bir graf içerisinde tüm düğümleri kapsayan minimum maliyete sahip ağacı elde etmektir.

Aşağıda kabaca algoritmanın çalışmasını anlayabilirsiniz.

1. Tüm kenarları maliyetlerine göre küçükten büyüğe doğru sıralay
2. En düşük maliyetli kenarı seçin ve oluşturduğunuz ağaçta çevrim oluşturup oluşturmadığını kontrol edin.Eğer içermiyorsa kenarı ağaca ekleyin.
    1. adımı işlem tamamlanana kadar devam ettirin.

Minimum spanning tree `(V-1)` adet kenar içerecektir.

Çevrim oluşturmak ne demektir? Eğer başladığınız bir noktadan dönüp dolaşıp ağaç üzerinde tekrar aynı noktaya gelebiliyorsanız çevrim oluşmuş demektir. Çevrim olup olmadığının anlanması özel bir konudur. Bununla ilgili yazılarımı ilerleyen zamanlarda yazacağım. `Union-Find` algoritması kullanılır.Mantık olarak çok basittir.

Çözüm aşağıdaki gibi olur

```
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
```

Bu algoritmanın zaman karmaşası `O(ElogE)` veya `O(ElogV)` olur.
