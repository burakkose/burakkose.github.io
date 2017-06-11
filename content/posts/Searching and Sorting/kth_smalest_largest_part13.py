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
