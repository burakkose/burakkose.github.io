Title: Sıralı olarak verilmiş üç diziden ortak elemanları bulma - Arama Algoritması
Date: 2015-10-18 18:00
Author: Burak
Category: Algoritma
Tags: algorithm, searching
Slug: search-common-element-three

Artan sırada verilmiş üç dizi içerisinde bulunan ortak elemanı bulmamıza yarayan algoritmaya bakacağız.

Örneğin
```
ar1[] = {1, 5, 10, 20, 40, 80}
ar2[] = {6, 7, 20, 80, 100}
ar3[] = {3, 4, 15, 20, 30, 70, 80, 120}
Output: 20, 80

ar1[] = {1, 5, 5}
ar2[] = {3, 4, 5, 5, 10}
ar3[] = {5, 5, 10, 20}
Output: 5, 5
```

Basit olarak ilk çözüm [link!](http://www.geeksforgeeks.org/union-and-intersection-of-two-sorted-arrays-2/) algoritmasını uygulamak ve elde edilen değerleri yedek bir dizi içerisinde tutmaktır. Bu çözüm ile karmaşıklık O(n1+n2+n3) olacaktır.

Yukarıda ki çözüm ekstra olarak hafıza ve iki adet döngü içermektedir. Oysa bu soruyu tek bir döngüde ve ektra hafıza gerektirmeden çözebiliriz.

Çözüm aşağıdaki gibidir.

```
def find_common(ar1, ar2, ar3):
    i, j, k = 0, 0, 0
    n1, n2, n3 = len(ar1), len(ar2), len(ar3)
    while i < n1 and j < n2 and k < n3:
        if ar1[i] == ar2[j] and ar2[j] == ar3[k]:
            print(ar1[i])
            i, j, k = i + 1, j + 1, k + 1
        elif ar1[i] < ar2[j]:
            i += 1
        elif ar2[j] < ar3[k]:
            j += 1
        else:
            k += 1

if __name__ == '__main__':
    ar1 = [1, 5, 10, 20, 40, 80]
    ar2 = [6, 7, 20, 80, 100]
    ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
    find_common(ar1, ar2, ar3)
```

Karmaşıklık O(n1+n2+n3) olacaktır.
