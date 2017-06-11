def count_zeros(n):
    result = 0
    i = 5
    while n // i >= 1:
        result += n // i
        i *= 5
    return result

if __name__ == '__main__':
    n = 100
    print(count_zeros(n))
