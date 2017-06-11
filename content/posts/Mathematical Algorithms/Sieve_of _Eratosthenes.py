def mark(arr, n):
    i = 2
    num = i * n
    while num <= len(arr):
        arr[num - 1] = 1
        i += 1
        num = i * n


def sieve_of_eratosthenes(n):
    if n >= 2:
        arr = [0] * n
        for i in range(1, n):
            if arr[i] == 0:
                print(i + 1)
                mark(arr, i + 1)

if __name__ == '__main__':
    n = 10
    sieve_of_eratosthenes(n)
