Title: Sayının faktoriyelinde sonda bulunan 0'ların sayısı - Matematik Problemi
Date: 2015-10-20 14:00
Author: Burak
Category: Algoritma
Tags: algorithm, mathematical
Slug: faktoriyel-0s-count

Verilen sayının faktoriyelinde sonda bulunan sıfırların sayısını bulmamız gerekiyor.

Örneğin;

```
Input: n = 5
Output: 1
5! = 20

Input: n = 20
Output: 4
20! = 2432902008176640000

Input: n = 100
Output: 24
```

En basit hali ile çözüm, sayının faktoriyelini hesaplamak ve sondaki sıfıların sayısını saymak. Masraflı ve büyük sayılar için çalışmayacak bir yöntem.

Matematikten faydalanarak şu şekilde çözebiliriz. Sayının sonunda 0 oluşabilmesi için en az bir adet 2 ve bir adet 5 gerekmektedir. Dolayısı ile sayı içerisindeki 2lerin ve 5lerin sayısını sayarsak çözüme ulaşabiliriz.

```
n = 5: Bir adet 5 ve üç adet 2 bulunmaktadır (2 * 2 * 2 * 3 * 5). Dolayısıyla 0ların sayısı 1'dir.

n = 11: İki adet 5 ve üç adet 2 bulunmaktadır. (2^8 * 3^4 * 5^2 * 7). Dolayısıyla 0ların sayısı 2'dir.
```

Sayı içerisindeki 2lerin sayısı es geçebiliriz zaten her seferinde elimizde fazladan 2 olacak. Sadece 5lerin sayısını saymak yeterlidir. Dikkat etmemiz gereken başka bir durum bulunmaktadır. Örneğin 28! sayısı için 25 sayısından gelen fazladan bir 5 durumu vardır. Aynı durum 125 yani 5'in üsleri içinde geçerlidir.

`n! için sondaki sıfır sayısı = floor(n/5) + floor(n/25) + floor(n/125) + ....`

```
def count_zeros(n):
    result = 0
    i = 5
    while n // i >= 1:
        result += n // i
        i *= 5
    return result

if __name__ == '__main__':
    n = 100
    print(count_zeros(n))
```
