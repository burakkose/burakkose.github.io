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
