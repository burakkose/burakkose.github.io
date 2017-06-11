Title: Suffix Array - String Algoritmaları
Date: 2015-10-18 18:00
Author: Burak
Category: Algoritma
Tags: algorithm, string, searching
Slug: suffix-array

Suffix dizisi, verilmiş olarak verilen stringe ait tüm suffixlerin alfabetik olarak sıralanmış halidir. Suffix array eğer elinizde bir suffix tree varsa, bu ağaç üzerinde DFS algoritmasını işletilmesi ile elde edilebilir.

Suffix array veri yapısının, suffix tree'den avantajları, geliştirilmiş bellek performansı ve keşleme özelliğidir.

Önreğin;

```
"banana" için.

0 banana                          5 a
1 anana     Suffixes sırala       3 ana
2 nana      ---------------->     1 anana  
3 ana        alfabetik olarak     0 banana  
4 na                              4 na   
5 a                               2 nana

"banana" için suffix dizisi {5, 3, 1, 0, 4, 2} olur.
```

### Suffix Array oluşturmak için temel metot

Açıkçası yukarıdaki örnek yeterince açık, basit bir kaç core fonksiyon sayesinde oluşturulabilecek bir algoritma. Ben biraz işin kolayına kaçarak Python'da basit şekilde oluşturacağım.

```
def build_suffix_array(text):
    return sorted(range(len(text)), key=lambda x: text[x:])
```

Yukarıdaki algoritma `O(n^2logn)` zaman karmaşıklığında çalışmaktadır. Suffix array oluşturmak içi çok daha verimli algoritmalar bulunmaktadır!

### Arama işlemi

Elimizde aslında sıralanmış bir string dizisi var gibi düşünebiliriz ve sıralanmış bir dizi içerisinde arama yapma işleminde herkesin muhtemelen aklına gelen algoritma `Binary Search` algoritmasıdır. Bu işlemdede bu algoritmayı kullanacağız.

Çözüm aşağıdaki gibi olacaktır.

```
def search(text, pattern, suffs, l, r):
    if r < l:
        return -1

    mid = l + (r - l) // 2
    t = text[suffs[mid]:][:len(pattern)]

    if pattern == t:
        return suffs[mid]
    elif pattern > t:
        return search(text, pattern, suffs, mid + 1, r)
    else:
        return search(text, pattern, suffs, l, mid - 1)

if __name__ == '__main__':
    text = "banana"
    pattern = "anan"
    suffix_array = build_suffix_array(text)
    print(search(text, pattern, suffix_array, 0, len(text) - 1))
```

Yukarıdaki arama algoritması `O(mlogn)`'dir. Gerçek şu ki suffix array veri yapısı için çok daha verimli tanımlamalar vardır. Bu gerçekten çok basit bir giriştir ve olayın genel mantığı için
