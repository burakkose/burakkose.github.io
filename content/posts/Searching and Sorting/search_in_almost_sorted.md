Title: Neredeyse sıralı dizi içerisinde arama - Arama Algoritması
Date: 2015-10-10 18:00
Author: Burak
Category: Algoritma
Tags: algorithm, searching
Slug: almost-sorted-search

Ufak bir işlem sonrası sıralanmış dizinin bazı elemanlarının yerleri karıştırılıyor. Örneğin `i.` pozisyonda olması gereken eleman `i-1` ya da `i+1` pozisyonunda bulunuyor. Hedef olarak verilen sayının dizi içerisindeki pozisyonunun bulunması amaçlanıyor.

Örneğin;
```
Input: arr[] =  {10, 3, 40, 20, 50, 80, 70}, key = 40
Output: 2

Input: arr[] =  {10, 3, 40, 20, 50, 80, 70}, key = 90
Output: -1
```

Klasik olarak en ilkel çözüm, tüm diziyi boydan boya aramaktır. `O(n)` karmaşıklığa sahiptir.

Bu çözümde ise sıralı diziler üzerinde uygulanan algoritmalardan olan `binary search` algoritmasının biraz daha modifiye edilmiş halini kullanacağız.

Fikir olarak şuna dayanmaktadır; elimizdeki değeri ortandaki üç eleman ile karşılaştıracağız. Geri mantık `binary search` algoritması gibidir.

Çözüm aşağıdadır.

```
def mod_binary_search(arr, l, r, x):
    '''Modifiye edilmiş binary search'''
    if r >= l:
        mid = l + (r - l) // 2

        # orta 3 eleman ile karşılaştırma
        if arr[mid] == x:
            return mid
        if mid > l and arr[mid - 1] == x:
            return mid - 1
        if mid < r and arr[mid + 1]:
            return mid + 1

        # Eğer eleman ortancadan küçükse, sola doğru kaydır
        if arr[mid] > x:
            return mod_binary_search(arr, l, mid - 2, x)
        # Aksi halde sağa doğru kaydır
        return mod_binary_search(arr, mid + 2, r, x)
    # Bulunamadı
    return -1

if __name__ == '__main__':
    arr = [3, 2, 10, 4, 40]
    target = 4
    result = mod_binary_search(arr, 0, len(arr) - 1, target)
    if result != -1:
        print(result)
    else:
        print("bulunamadi")
```

Algoritmanın karmaşıklığı `O(logn)` olur.
