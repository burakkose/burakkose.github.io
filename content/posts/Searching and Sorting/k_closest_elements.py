def find_cross_point(arr, low, high, x):
    # x tüm elemanlardan büyükse
    if arr[high] <= x:
        return high
    # x tüm elemanlardan küçükse
    if arr[low] > x:
        return low

    # Orta noktayı bulma
    mid = (low + high) // 2

    # X ortanca elemansa
    if arr[mid] <= x and arr[mid + 1] > x:
        return mid

    # x < arr[mid] ve x < arr[mid+1] ise
    if arr[mid] < x:
        return find_cross_point(arr, mid + 1, high, x)

    return find_cross_point(arr, low, mid - 1, x)


def print_closest(arr, x, k):
    l = find_cross_point(arr, 0, len(arr) - 1, x)
    r, count = l + 1, 0

    # Eşit elemanları dikkate alma
    if arr[l] == x:
        l -= 1

    # Geçiş noktasından itibare sağ ve sol kontrolu
    while l >= 0 and r < len(arr) and count < k:
        if x - arr[l] < arr[r] - x:
            print(arr[l])
            l -= 1
        else:
            print(arr[r])
            r += 1
        count += 1

    # Sağ tarafta hiç eleman yoksa sol tarafı yazdır
    while count < k and l >= 0:
        print(arr[l])
        l, count = l - 1, count + 1

    # Sol tarafta hiç eleman yoksa sağ tarafı yazdır
    while count < k and r < len(arr):
        print(arr[r])
        r, count = r + 1, count + 1

if __name__ == '__main__':
    arr = [12, 16, 22, 30, 35, 39, 42,
           45, 48, 50, 53, 55, 56]
    target, k = 35, 4
    print_closest(arr, target, k)
