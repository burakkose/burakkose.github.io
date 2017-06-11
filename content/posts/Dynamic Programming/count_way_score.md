Title: Hedef puana kaç farklı şekilde ulaşılır? - Dinamik Programlama
Date: 2015-10-19 23:00
Author: Burak
Category: Algoritma
Tags: algorithm, dynamic programming
Slug: nth-score

3, 5 ve 10 puan almanın mümkün olduğu ve hedef puana bu puan gruplarını kullanarak kaç farklı şekilde ulaşılabileceğini bulacağız.

Örnek;

```
Input: n = 20
Output: 4
(10, 10)
(5, 5, 10)
(5, 5, 5, 5)
(3, 3, 3, 3, 3, 5)

Input: n = 13
Output: 2
(3, 5, 5)
(3, 10)
```

Çözüm mantığı gayet basittir. n+1 boyutunda bir dizi yaratılır ve her puanlama için döngüler ile tüm çözüm sayıları tutulur. Zaman ve yer karmaşıklığı 0(n) olacaktır.

```
def adjust(l, score, n):
    for i in range(score, n + 1):
        l[i] += l[i - score]


def count(n):
    result = [0] * (n + 1)
    result[0] = 1  # 0 puan için

    adjust(result, 3, n)
    adjust(result, 5, n)
    adjust(result, 10, n)

    return result[n]

if __name__ == '__main__':
    score = 20
    print(count(score))
```

Cevabı doğru bulduk fakat (10, 5, 5), (5, 5, 10) ve (5, 10, 5) durumları tek bir durum olarak sayılmıştır. Peki bu durumlarıda farklı birer yol olarak saymak istersek yukarıdaki kodu biraz değiştirmek gerekecek.

```
def count_new(n):
    result = [0] * (n + 1)
    result[0] = 1  # 0 puan için

    for i in range(3, n + 1):
        if i >= 3:
            result[i] += result[i - 3]
        if i >= 5:
            result[i] += result[i - 5]
        if i >= 10:
            result[i] += result[i - 10]

    return result[n]

if __name__ == '__main__':
    score = 20
    print(count_new(score))
```
