Title: Çarpma ve bölme işlemi kullanmadan üs alma - Matematik Problemi
Date: 2015-10-12 18:00
Author: Burak
Category: Algoritma
Tags: algorithm, mathematical
Slug: pow-without

Üs alma işlemi problemlerine farklı bir yaklaşım sunan bu problemde, çarpma(`*`) ve bölme(`/`) işlemi kullanmadan üs alma işlemine bakacağız.

Örneğin;
```
5^6 işlemi için;
result = 0
1.) 5 kere 5 ekle (5^2) = 25
2.) 5 kere 25 ekle (5^3) = 125
3.) 5 kere 125 ekle (5^4) = 625
4.) 5 kere 625 ekle (5^5) = 3125
5.) 5 kere 3125 ekle (5^6) = 15625
```
### İç içe döngü kullanarak

```
def nested_pow(a, b):
    if b == 0:
        return 1
    result, increment = a, a
    for i in range(1, b):
        for j in range(1, a):
            result += increment
        increment = result
    return result
```

### Recursive çözüm

```
def recursion_pow(a, b):
    if b != 0:
        return multiply(a, recursion_pow(a, b - 1))
    else:
        return 1


def multiply(x, y):
    if y != 0:
        return x + multiply(x, y - 1)
    else:
        return 0
```

```
if __name__ == '__main__':
    print(nested_pow(5, 6))
    print(recursion_pow(5, 3))
```
