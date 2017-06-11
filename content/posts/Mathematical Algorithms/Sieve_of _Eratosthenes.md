Title: Sieve of Eratosthenes - Matematik Problemi
Date: 2015-10-20 16:00
Author: Burak
Category: Algoritma
Tags: algorithm, mathematical
Slug: sieve-of-eratosthenes

Verilen bir `n` sayısı var ve bu sayıya kadar olan tüm asal sayıların elde edilmesi için sunulmuş en efektif çözümdür [(ref: Wiki)](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes).

![gif](https://upload.wikimedia.org/wikipedia/commons/b/b9/Sieve_of_Eratosthenes_animation.gif)

Algoritma şu şekilde çalışır.

1. 2'den n'e kadar bir liste yaratılır. (2,3,4,5,6...n)
2. p = 2 yapılarak ilk asal sayı 2 ilan edilir.
3. 2p,3p,4p,5p ... gibi katlar alınarak bu sayılar işaretlenir ve asal sayılardan dışlanmış olunur
4. iaşretlenmemiş ilk sayı bulunarak p'ye atanır ve işlemler tekrar edilir.

Çözüm aşağıdaki gibi olur.


```
def mark(arr, n):
    i = 2
    num = i * n
    while num <= len(arr):
        arr[num - 1] = 1
        i += 1
        num = i * n


def sieve_of_eratosthenes(n):
    if n >= 2:
        arr = [0] * n
        for i in range(1, n):
            if arr[i] == 0:
                print(i + 1)
                mark(arr, i + 1)

if __name__ == '__main__':
    n = 10
    sieve_of_eratosthenes(n)
```


Agoritmanın anlaşılırlığı için kod uzun tutulmuştur. Çok daha fazla kısaltılması mümkündür.
