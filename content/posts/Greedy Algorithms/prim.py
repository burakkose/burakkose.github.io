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
