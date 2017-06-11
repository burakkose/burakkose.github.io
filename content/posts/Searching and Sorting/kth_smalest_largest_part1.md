Title: K. küçük veya büyük sayısı bulmak - Part 1 - Arama Algoritması
Date: 2015-10-04 18:00
Author: Burak
Category: Algoritma
Tags: algorithm, searching
Slug: search-k-largest-or-smalest

Bir dizi ve `k` sayısı veriliyor(k < len(dizi)). Cevap olarak dizi içerisinde ki k. küçük veya büyük elemanın bulunması hedefleniyor.

Örneğin;

```
Input: arr[] = {7, 10, 4, 3, 20, 15}
       k = 3
Output: 7

Input: arr[] = {7, 10, 4, 3, 20, 15}
       k = 4
Output: 10
```

### Çözüm 1 (Basit Çözüm)
Akla gelen en basit çözm elimizdeki veri kümesini ihtiyaca göre sıralamak ve k. indeksi çağırmak. Sıralama için kullanılacak en verimli algoritma ortalama `O(nlogn)` zaman alacağı için karmaşıklık `O(nlogn)` olacaktır.

### Çözüm 2 (Min Heap – HeapSelect)
Bu problemi `O(nlogn)` zaman karma1şıklığından daha iyi bir şekilde çözebiliriz. Kullanacağımız algoritma, heap veri yapısı yardımı ile sonuca ulaşacaktır.

Çözüm aşağıdaki gibidir.

```
class MinHeap:

    def __init__(self, arr):
        self.harr = arr
        self.heap_size = len(arr)
        i = (self.heap_size - 1) // 2
        while i >= 0:
            self.min_heapify(i)
            i -= 1

    def min_heapify(self, i):
        l, r, smallest = self.left(i), self.right(i), i
        if l < self.heap_size and self.harr[l] < self.harr[i]:
            smallest = l
        if r < self.heap_size and self.harr[r] < self.harr[smallest]:
            smallest = r
        if smallest != i:
            self.harr[i], self.harr[smallest] = self.harr[
                smallest], self.harr[i]
            self.min_heapify(smallest)

    def extract_min(self):
        if not self.heap_size:
            return -1
        root = self.harr[0]
        if self.heap_size > 1:
            self.harr[0] = self.harr[self.heap_size - 1]
            self.min_heapify(0)
        self.heap_size -= 1
        return root

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def paremt(self, i):
        return (i - 1) // 2


def kth_smallest(arr, k):
    heap = MinHeap(arr)
    for i in range(k - 1):
        heap.extract_min()
    return heap.harr[0]

if __name__ == '__main__':
    arr = [12, 3, 5, 7, 19]
    print(kth_smallest(arr, 2))
```
Bu algoritmanın karmaşıklığı `O(n+klogn)` olacakır.

### Çözüm 3 (Max-Heap)
Çözüm 2'deki gibi, bu sefer max-heap ile problemi çözebiliriz.Karmaşıklık `O(k + (n-k)*logk)` olacaktır.
```
class MaxHeap:

    def __init__(self, arr):
        self.harr = arr
        self.heap_size = len(arr)
        i = (self.heap_size - 1) // 2
        while i >= 0:
            self.max_heapify(i)
            i -= 1

    def max_heapify(self, i):
        l, r, largest = self.left(i), self.right(i), i
        if l < self.heap_size and self.harr[l] > self.harr[i]:
            largest = l
        if r < self.heap_size and self.harr[r] > self.harr[largest]:
            largest = r
        if largest != i:
            self.harr[i], self.harr[largest] = self.harr[
                largest], self.harr[i]
            self.max_heapify(largest)

    def extract_max(self):
        if not self.heap_size:
            return -1
        root = self.harr[0]
        if self.heap_size > 1:
            self.harr[0] = self.harr[self.heap_size - 1]
            self.max_heapify(0)
        self.heap_size -= 1
        return root

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def paremt(self, i):
        return (i - 1) // 2


def kth_smallest(arr, k):
    heap = MaxHeap(arr)
    for i in range(len(arr) - k):
        heap.extract_max()
    return heap.harr[0]

if __name__ == '__main__':
    arr = [12, 3, 5, 7, 19]
    print(kth_smallest(arr, 2))
```
### Çözüm 4 (QuickSelect)
Bu çözüm, çözüm 1 de bahsedilen yöntemin optimize edilmiş halini yansıtmaktadır.Quick sort algoritmasının modifiye edilmesi ile elde edilmiştir. Pivot eleman seçeceğiz, bunu doğru pozisyona yerleştireceğiz ve etrafını parçalayacaız. En kötü durumda karmaşıklık `O(n^2)`, fakat ortalama durumda `O(n)` olacaktır.

```
from math import inf


def kth_smallest(arr, l, r, k):
    if k > 0 and k <= r - l + 1:
        pos = partition(arr, l, r)

        if pos - l == k - 1:
            return arr[pos]
        if pos - l > k - 1:
            return kth_smallest(arr, l, pos - 1, k)

        return kth_smallest(arr, pos + 1, r, k - pos + l - 1)

    return inf


def partition(arr, l, r):
    x, i = arr[r], l
    for j in range(l, r):
        if arr[i] <= x:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i

if __name__ == '__main__':
    arr = [12, 3, 5, 7, 4, 19, 26]
    print(kth_smallest(arr, 0, len(arr) - 1, 3))
```
