Title: Veri akışının aritmetik ortalaması - Matematik Problemi
Date: 2015-10-14 18:00
Author: Burak
Category: Algoritma
Tags: algorithm, mathematical
Slug: stream-ortalama

Bu problemde elimize, bir kaynaktan gelen sürekli veriler var yani hep bir sayı akışı var. Bizden her gelen yeni sayı için o anki aritmetik ortalama istenmektedir.

Örneğin;

```
Akış ... 10, 20, 30, 40, 50, 60, …
10 geldiğinde ortalama 10.00
20 geldiğinde ortalama 15.00
30 geldiğinde ortalama 20.00
40 geldiğinde ortalama 25.00
50 geldiğinde ortalama 30.00
60 geldiğinde ortalama 35.00
..................
```
Çözüm şu şekilde olacaktır.

```
def get_avg(prev, num, count):
    return (prev * count + num) / (count + 1)


def calculate_stream(arr):
    avg = 0
    for i, num in enumerate(arr):
        avg = get_avg(avg, num, i)
        print(num, " geldiğinde ortalama = ", avg, sep="")

if __name__ == '__main__':
    arr = [10, 20, 30, 40, 50, 60]
    calculate_stream(arr)
```
