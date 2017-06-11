Title: En uzun ortak altdizi(LCS) - Dinamik Programlama
Date: 2015-10-20 18:00
Author: Burak
Category: Algoritma
Tags: algorithm, dynamic programming, bioinformatic
Slug: lcs

Bilgisayar bilimlerinde önemli bir yere sahip olan bu problemde, verilen iki dizgide de ortak olarak bulunan ve aynı yönde sıralanmış dizgiler bütünü elde edilmeye çalışılmaktadır.

Örneğin;


```
 “ABCDGH” ve “AEDFHR” için “ADH”
 “AGGTAB” ve “GXTXAYB” için “GTAB”
```


Dosyalar arasındaki farkları, değişiklikleri elde etmede ve özellikle bioinformatik alanında sıkça karşılaşılan bir çözümdür. Çözüm aşağıdaki gibidir.


```
def lcs(s1, s2):
    len_s1, len_s2 = len(s1) + 1, len(s2) + 1
    S = [[0] * len_s1 for _ in range(len_s2)]

    for i in range(1, len_s2):
        for j in range(1, len_s1):
            if s1[j - 1] == s2[i - 1]:
                S[i][j] = S[i - 1][j - 1] + 1
            else:
                S[i][j] = max(S[i - 1][j], S[i][j - 1])

    return S[len_s2 - 1][len_s1 - 1]

if __name__ == '__main__':
    X = "AGGTAB"
    Y = "GXTXAYB"
    print(lcs(X, Y))
```


Bu algoritmanın zaman karmaşıklığı `O(nm)`'dir. Peki hangi dizginin LCS olduğunu bulmak için ne yapmamız gerekiyor? Bunun için şu şekilde bir düzenleme ile sonuca ulaşabiliriz.


```
def lcs(s1, s2):
    len_s1, len_s2 = len(s1) + 1, len(s2) + 1
    S = [[0] * len_s1 for _ in range(len_s2)]

    for i in range(1, len_s2):
        for j in range(1, len_s1):
            if s1[j - 1] == s2[i - 1]:
                S[i][j] = S[i - 1][j - 1] + 1
            else:
                S[i][j] = max(S[i - 1][j], S[i][j - 1])

    i, j = len_s2 - 1, len_s1 - 1
    result = ""
    while i > 0 and j > 0:
        if s1[j - 1] == s2[i - 1]:
            result += s1[j - 1]
            i, j = i - 1, j - 1
        elif S[i - 1][j] > S[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return S[len_s2 - 1][len_s1 - 1], result[::-1]

if __name__ == '__main__':
    X = "AGGTAB"
    Y = "GXTXAYB"
    print(lcs(X, Y))
```


Çok daha ayrıntılı bir inceleme için [Wiki](https://en.wikipedia.org/wiki/Longest_common_subsequence_problem) sayfasından yardım alabilirsiniz.
