Title: En uzun artan altdizi(LIS) - Dinamik Programlama
Date: 2015-10-23 21:00
Author: Burak
Category: Algoritma
Tags: algorithm, dynamic programming
Slug: lis

Bir dizi içerisinde en uzun artan altdiziyi bulmayı amaçlayan bir problemdir. Örneğin

```
Input:
    {10, 22, 9, 33, 21, 50, 41, 60, 80}
Output:
    6{10, 22, 33, 50, 60, 80}
```

[LCS]({filename}../Dynamic Programming/lcs.md) algoritmasına benzer bir yol izleyeceğiz. Kod anlaşılır durumda, çözüm aşağıdadır.

```
def lis(arr):
    lis = [1] * len(arr)

    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    return max(lis)

if __name__ == '__main__':
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    print(lis(arr))
```

Yukarıdaki algoritmanın zaman karmaşıklığı `O(n^2)`'dir. Algoritma farklı bir yaklaşım ile `O(nlogn)` karmaşıklık ile çözülebilir. İncelemek için : [link](http://en.wikipedia.org/wiki/Longest_increasing_subsequence#Efficient_algorithms)
