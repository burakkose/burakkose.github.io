Title: Sayı fibonacci sayısı mı? - Matematik Problemi
Date: 2015-10-12 18:00
Author: Burak
Category: Algoritma
Tags: algorithm, mathematical
Slug: fibo-kontrol

Verilen sayının fibonacci sayısı olup olmadığını anlamanın basit bir yolu var.

İsterseniz sırayla kendi sayınıza kadar fibonacci sayılarını oluşturup kontrol ederek gidebilirsiniz. Tabi aşırı maliyetli bir çözüm olur, ya da matematikten faydalanırsınız.

Bu çözüme tam kare çözümü denmektedir. Kontrol için aşağıdaki eşitliği kullancağız.

`(5*n^2 + 4) veya (5*n^2 – 4) `

```
def is_perfect_square(x):
    s = x ** 0.5
    return s * s == x


def is_fibo(n):
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

if __name__ == '__main__':
    number = 34
    print(is_fibo(number))
```
