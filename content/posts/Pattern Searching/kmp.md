Title: KMP Algoritmasi - String Algoritmaları
Date: 2015-10-07 18:00
Author: Burak
Category: Algoritma
Tags: algorithm, string, searching
Slug: kmp

Bir diğer string arama algoritmalarından olan `KMP` algoritmasına bakacağız.

Örnek olarak;
```
txt =  "THIS IS A TEST TEXT"
pat = "TEST"
Output : 10
```
ve

```
txt =  "AABAACAADAABAAABAA"
pat = "AABA"
Output : 0, 9, 13
```

Bir önceki [yazıda]({filename}naive_pattern_search.md) en kaba hali ile bir text içerisinde nasıl başka bir text aramasının yapılacağını incelemiştik. O algoritma `O(m*(n-m+1))` karmaşıklığa sahipti. Bu algoritmanın en kötü durumda karmaşıklığı `O(n)`'dir.

### KMP (Knuth Morris Pratt)

Kısaca yapılan iş şu şekilde yürümektedir. Ne zaman bir eşleşmeme duruöu olursa, elimizde daha önce elde ettiğimiz bilgileri kullanarak, deseni kaydırma ve benzetme işlemi yaparız. Dolayısı ile gereksiz karşılaştırmadan kaçtığımız için zaman karmaşıklığından kazanmış oluruz.

LPS için aşağıdaki örnelere bakın.
```
 “AABAACAABAA”, lps = [0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 5]
 “ABCDE”, lps = [0, 0, 0, 0, 0]
 “AAAAA”, lps = [0, 1, 2, 3, 4]
 “AAABAAA”, lps = [0, 1, 2, 0, 1, 2, 3]
 “AAACAAAAAC”, lps = [0, 1, 2, 0, 1, 2, 3, 3, 3, 4]
```
İşleyiş aşağıdaki kod ile daha iyi anlaşılacaktır.

```
 def KMP_search(text, pattern):
     lps = compute_lps_array(pattern)
     m, n, j = len(pattern), len(text), 0
     i = 0  # text indeksi
     while i < n:
         if pattern[j] == text[i]:
             i, j = i + 1, j + 1
         if j == m:
             print(i - j)
             j = lps[j - 1]
         elif i < n and pattern[j] != text[i]:
             # j eşleşme sonrası eşleşmeme
             if j != 0:
                 j = lps[j - 1]
             else:
                 i += 1


 def compute_lps_array(pattern):
     lps = [0] * len(pattern)
     # len_sp = son en uzun prefix suffix uzunluğu
     len_sp, i, len_pattern = 0, 1, len(pattern)

     while i < len_pattern:
         if pattern[i] == pattern[len_sp]:
             len_sp += 1
             lps[i] = len_sp
             i += 1
         elif len_sp != 0:
             len_sp = lps[len_sp - 1]
         else:  # len_sp == 0
             lps[i] = 0
             i += 1

     return lps

 if __name__ == '__main__':
     text = "ABABDABACDABABCABAB"
     pattern = "ABABCABAB"
     KMP_search(text, pattern)
```
