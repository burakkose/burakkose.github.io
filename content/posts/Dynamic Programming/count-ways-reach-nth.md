Title: N. basamağa kaç adımda ulaşılabilir? - Dinamik Programlama
Date: 2015-10-19 23:00
Author: Burak
Category: Algoritma
Tags: algorithm, dynamic programming
Slug: nth-stair

N adet basamağa sahip bir merdivende, en alt noktadan üst noktaya her seferinde en fazla bir veya iki adım atarak kaç farklı şekilde ulaşabileceğimizi bulacağız.

![basamak](/images/DynamicProgramming/stairs.gif) Örneğin yadaki resim için 3 adet çözüm vardır.

Daha fazla örnek;

```
Input: n = 1
Output: 1
Sadece 1 adımda ulaşılır

Input: n = 2
Output: 2
İki farklı adımda ulaşılır: (1, 1) ve (2)

Input: n = 4
Output: 5
(1, 1, 1, 1), (1, 1, 2), (2, 1, 1), (1, 2, 1), (2, 2)
```

Basit olarak rekürsif olarak çözebilir. `yol(n) = yol(n-1) + yol(n-2)` . Aslında yandaki formulun [fibonacci]({filename}../Mathematical Algorithms/fibonacci.md) formulu olduğu çok belli.

```
def recursion(n):
    if n <= 1:
        return n
    return recursion(n - 1) + recursion(n - 2)


def solve(n):
    return recursion(n + 1)

if __name__ == '__main__':
    n = 4
    print(solve(n))
```

Yukarıdaki çözüm O(2^n) zaman karmaşasına sahiptir. Tabi çok daha efektif çözmenin yollarını [şurada]({filename}../Mathematical Algorithms/fibonacci.md) daha önce belirttim.

#### Problemin genelleştirilmiş hali
Örneğin kişinin m adıma kadar hakkı olsun. m=4 için kişi her bir anda 1, 2, 3 veya 4 adım atabilir.
`yol(n, m) = yol(n-1, m) + yol(n-2, m) + ... yol(n-m, m) `

```
def calculate(n, m):
    if n <= 1:
        return n
    res = 0
    i = 1
    while i <= m and i <= n:
        res += calculate(n - i, m)
        i += 1
    return res


def solve_gen(n, m):
    return calculate(n + 1, m)

if __name__ == '__main__':
    basamak = 4
    adim = 2
    print(solve_gen(basamak, adim))
```
