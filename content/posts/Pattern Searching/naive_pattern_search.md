Title: En basit hali ile text arama işlemi - String Algoritmaları
Date: 2015-10-11 18:00
Author: Burak
Category: Algoritma
Tags: algorithm, string, searching
Slug: naive-search-string

Text işlemlerinde, bir dizgi içerisinde dizgi aramadaki en basit çözümü inceleyeceğiz.

```
txt[] =  "THIS IS A TEST TEXT"
pat[] = "TEST"
Output: 10
```

```
txt[] =  "AABAACAADAABAAABAA"
pat[] = "AABA"
Output: 0,9,13
```
Çözüm aşağıdaki gibi olacaktır.

```
def search(text, pattern):
    m, n = len(pattern), len(text)
    for i in range(n - m + 1):
        for j in range(m):
            if text[i + j] != pattern[j]:
                break
        if j + 1 == m:
            print(i)

if __name__ == '__main__':
    txt = "AABAACAADAABAAABAA"
    pat = "AABA"
    search(txt, pat)

```

### En iyi durum nedir?
```
txt[]  = "AABCCAADDEE"
pat[] = "FAA"
```
Desenin ilk karakteri arana text içerisinde bulunmadığı zamandır ve karmaşıklık `O(n)` olur.

### En kötü durum nedir?
```
txt[] = "AAAAAAAAAAAAAAAAAA"
pat[] = "AAAAA"
```
Yani tüm karakterler aynı olduğunda ve

```
txt[] = "AAAAAAAAAAAAAAAAAB"
pat[] = "AAAAB"
```
son karakterler aynı olursa. Bu durumda da karmaşıklık `O(m*(n-m+1))` olur.

String arama işlemlerinin önemli olduğunu söylemiştim. Bu gördüğünüz algoritma adı üstünde en kaba,basit çözümdür. Çok daha efektif algoritmalar bulunmaktadır.
