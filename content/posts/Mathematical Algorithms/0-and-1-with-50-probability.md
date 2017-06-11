Title: Hileli parayı hilesiz yapmak - Matematik Problemi
Date: 2015-10-20 12:00
Author: Burak
Category: Algoritma
Tags: algorithm, mathematical
Slug: 0-1-50

Verilen bir fonksiyon yazı tura işlemini %60 yazı %40 tura gelecek şekilde gerçekleştiriyor. Bu verilen fonksiyonu kullanarak bu işlemi nasıl hilesiz yapabiliriz?

Paranın %60 olasılıkla 0, %40 olasılık ile 1 döndürdüğünü biliyoruz. Çözüm olarak bu fonksiyonu iki kere çağıracağız. Eğer sonuçlar (1,0) veya (0,1) ise problem yok, direk cevabı vereceğiz fakat cevaplar (1,1) veya (0,0) ise işlemi tekrarlayacağız.

```
(0, 1): 0 sonrası 1 gelme olasılığı = 0.6 * 0.4 = 0.24
(1, 0): 1 sonrası 0 gelme olasılığı = 0.4 * 0.6 = 0.24
```

```
def foo():
    'Bu method hileli olarak 1 veya 0 döndürür'
    pass


def my_foo():
    val1 = foo()
    val2 = foo()
    if val1 == 0 and val2 == 1:
        return 0  # 0.24 olasılık
    if val1 == 1 and val2 == 0:
        return 1  # 0.24 olasılık
    return my_foo()  # 1 - 0.24 - 0.24 olasılık
```
