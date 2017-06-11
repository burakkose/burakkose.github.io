Title: Prim Algoritması - Greedy Yaklaşımı
Date: 2015-10-14 18:00
Author: Burak
Category: Algoritma
Tags: algorithm, greedy, graph theory
Slug: prim-mst

Tıpkı Kruskal algoritmasında olduğu gibi Prim algoritmasında da amaç en kısa yol ağacını bulmaktır ve greedy yaklaşımı ile çözülür.

Algoritma aşağıdaki şekilde çalışır.

1. Ağaca eklenmiş tüm düğümleri tutacak bir küme oluştur(`mst_set`).
2. Başlangıçta tüm düğümlere sonsuz değeri verin sadece içlerinden bir tanesini seçmek için 0 değeri verin.
3. Eğer `1.` adımda oluşturduğunuz küme tüm düğümleri kapsamıyorsa
    1. `mst_set` 'in içermediği ve minimum değere sahip düğümü seçin(`u`)
    2. `u` 'yu `mst_set` içerisine atın
    3. `u` 'ya komşu olan tüm düğümlerin değerini güncelleyin.Tüm komşu düğümler(`v`) üzerinde güncelleme amacıyla gezinirken eğer u-v önceki değerden küçükse değeri u-v şeklinde güncelleyin.

Şimdi algoritmayı uygulamaya geçelim.

```
from math import inf


def min_key(key, mst_set):
    '''Geriye minimum değere sahip komşunun indeksini döndürür'''
    mini, min_index = inf, inf
    for index, vertex in enumerate(mst_set):
        if not vertex and key[index] < mini:
            mini, min_index = key[index], index
    return min_index


def print_prim(graph):
    # Düğüm sayısı
    vertices_len = len(graph)

    # Oluşturulmuş ağac listesi
    parent = [None] * vertices_len

    # Minimum ağırlıklı komşuyu seçmek için kullanılan liste
    key = [inf] * vertices_len

    # Ağaca eklenmemiş düğümleri içeren liste
    mst_set = [False] * vertices_len

    key[0] = 0  # İlk düğüm seçiliyor
    parent[0] = - 1  # İlk düğüm her zaman root'dur

    for count in range(vertices_len - 1):
        # Minimum değere sahip komşu
        u = min_key(key, mst_set)

        # Ağaca eklenmiş olduğu işaretleniyor
        mst_set[u] = True

        # Güncelleme işlemi
        for v in range(vertices_len):
            if graph[u][v] and not mst_set[v] and graph[u][v] < key[v]:
                parent[v], key[v] = u, graph[u][v]

    print("Edge   Weight")
    for i in range(1, vertices_len):
        print(parent[i], " - ", i, "  ", graph[i][parent[i]])

if __name__ == '__main__':
    """
          2    3
       (0)--(1)--(2)
        |   / \   |
       6| 8/   \5 |7
        | /     \ |
       (3)-------(4)
              9
    """
    graph = [[0, 2, 0, 6, 0],
             [2, 0, 3, 8, 5],
             [0, 3, 0, 0, 7],
             [6, 8, 0, 0, 9],
             [0, 5, 7, 9, 0],
             ]
    print_prim(graph)
```

Algoritmanın zaman karmaşıklığı `O(n^2)` 'dir. Eğer girdi olarak alınan graf komşuluk matrisi yerine binary heap hardımıyla liste şeklinde kullanılmış olsaydı karmaşıklık `O(ElogV)` olacaktı.
