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
