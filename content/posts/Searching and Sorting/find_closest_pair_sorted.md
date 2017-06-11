Title: Sıralı iki dizi içerisinde seçilen ikili toplamının hedef sayıya en yakın olması - Arama Algoritması
Date: 2015-10-17 18:00
Author: Burak
Category: Algoritma
Tags: algorithm, searching
Slug: find-closest-pair-sorted

Hoşuma giden problem türlerinden olan yakın ikili sorularından biri. Bu problemde girdi olarak verilen iki tane sıralanmış dizi ve bir hedef numarası bulunuyor ve dizilerden seçilen hangi iki elemanın toplamının hedef elemana en yakın sayı olacağını bulmamız gerekiyor.

Örnek olarak;

```
Input:  ar1[] = {1, 4, 5, 7};
        ar2[] = {10, 20, 30, 40};
        x = 32      
Output:  1 and 30

Input:  ar1[] = {1, 4, 5, 7};
        ar2[] = {10, 20, 30, 40};
        x = 50      
Output:  7 and 40
```
gibi.

Eğer dizilerin birinin `n` elemanlı diğerinin `m` elemanlı (n=m olabilir) olduğunu varsayarsak en ilkkel çözüm şu şekilde olacaktır. İki tane döngü kurarak karşılıklı olarak tüm ihtimalleri deneyerek cevaba ulaşmaya çalışırız. Tabi bu çözümde verilen dizilerin sıralı olup olmamasının bir değeri kalmamakla birlikte zaman karmaşıklığımız `O(n^2)` olacaktır.

Şimdi başka bir taraftan probleme bakalım.Verilen dizileri aynı merge sort işleminde olduğu gibi birleştirelim ve tek bir dizi üzerinden hedef elemana ulaşmaya çalışabiliriz(buda özel bir problem). Bunun sayesinde karmaşıklık `O(n)` dolaylarına inecektir ve ekstra memory kullanmış olacağız.

Peki çok daha iyi bir çözüm yok mu?

1. Karşılaştırma için `diff` adında sonsuz değere sahip bir değişken ata
2. Sıralı olarak verilen diziler üzerinde gezinmek için `l` ve `r` adında ki index değişkeni tutun
1. l = 0 ve r = -1
3. Döngü şartı l < m ve r >= 0 olmak üzere
1. Eğer abs(ar1[l] + ar2[r] - sum) < diff ise diff ve result değişkenlerini güncelle
2. Eğer ar1[l] + ar2[r] <  sum ise l++
3. r--

Çözüm aşağıdaki gibi olacaktır.

```
from math import inf


def print_closest(ar1, ar2, x):
    diff = inf
    res_l, res_r = -1, -1
    l, r = 0, len(ar2) - 1

    while l < len(ar1) and r >= 0:
        if abs(ar1[l] + ar2[r] - x) < diff:
            resl_l, res_r, diff = l, r, abs(ar1[l] + ar2[r] - x)

        if ar1[l] + ar2[r] > x:
            r -= 1
        else:
            l += 1

    print("({} - {})".format(ar1[res_l], ar2[res_r]))

if __name__ == '__main__':
    ar1 = [1, 4, 5, 7]
    ar2 = [10, 20, 30, 40]
    x = 38
    print_closest(ar1, ar2, x)
```
