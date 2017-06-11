Title: Girilen sayıdan bir sonraki büyük sayıyı bulma - Matematik Problemi
Date: 2015-10-08 18:00
Author: Burak
Category: Algoritma
Tags: algorithm, mathematical
Slug: next-num

String olarak verilen sayının bir sonraki büyük saıyı ekrana bastıran, eğer şartlar uygun değilse imkansız yazan problemi inceleyeceğiz.

```
Input:  n = "218765"
Output: "251678"

Input:  n = "1234"
Output: "1243"

Input: n = "4321"
Output: "Imkansız"

Input: n = "534976"
Output: "536479"
```

Çözüm için;

1. Eğer tüm sayılar azalan sırada ise 'Imkansız' basılır.
2. Eğer tüm sayılar artan sırada ise son iki sayı ver değiştirecektir.
3. Diğer sayılar için
    1. Sayının birler basamağından başlanarak diğer haneleri incelenir. Birber basamağından daha değerli basamaklara doğru artışı bozacak hane aranır. Örneğin “534976” sayısı için `4` olan basamak bu durumu sağlar.(6<7<9)
    2. Sayı 53,4,976 şeklinde bölünür ve 4'ün sağ tarafında kalan sayılardan 4'den büyük olan en küçük sayı bulunur(6'dır).
    3. 4 ve 6 yer değişir("53,6,974" olur).
    4. "974" olan kısım sıralanır ve son olarak cevap "536479" olur.

Çözüm aşağıdaki gibi olacaktır.

```
def find_next(num):
    for i in range(len(num) - 1, 0, -1):
        if num[i] > num[i - 1]:
            break

    if i - 1 == 0:
        print("Imkansiz")
        return

    x, smallest = num[i - 1], i
    for j in range(i + 1, len(num)):
        if num[j] > x and num[j] < num[smallest]:
            smallest = j

    num = list(num)
    num[smallest], num[i - 1] = num[i - 1], num[smallest]

    num[i:] = sorted(num[i:])
    print(''.join(num))

if __name__ == '__main__':
    find_next("534976")
    find_next("4321")

```
