Title: Bozuk para problemi - Greedy Yaklaşımı
Date: 2015-10-13 18:00
Author: Burak
Category: Algoritma
Tags: algorithm, greedy
Slug: bozuk-para

Bize verilen bir miktar para var ve bu miktarı en az sayıda banknot ile karşılamak istiyoruz. Gerçek hayattada sıkça karşılaşılan bir problemi aslında greedy yaklaşımı ile çözüyoruz.

Örneğin

```
Input: V = 70 TL
Output: 2
50 TL + 20 TL = 70 TL

Input: V = 121 TL
Output: 3
100 TL + 20 TL + 1 TL = 121 TL
```

Mantık çok basit değil mi? Şimdi çözüme geçelim

```
MONEY = (1, 2, 5, 10, 20, 50, 100, 200)


def find_min(target):
    result = []
    for m in sorted(MONEY, reverse=True):
        while target >= m:
            target -= m
            result.append(m)
    print(*result, sep=" Tl + ", end=" = {} TL".format(sum(result)))

if __name__ == '__main__':
    target = 1994
    find_min(target)
```
