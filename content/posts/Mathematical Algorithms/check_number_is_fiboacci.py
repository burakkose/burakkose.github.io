def is_perfect_square(x):
    s = x ** 0.5
    return s * s == x


def is_fibo(n):
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

if __name__ == '__main__':
    number = 34
    print(is_fibo(number))
