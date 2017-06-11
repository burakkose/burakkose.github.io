def recursion(n):
    if n <= 1:
        return n
    return recursion(n - 1) + recursion(n - 2)


def solve(n):
    return recursion(n + 1)


def calculate(n, m):
    if n <= 1:
        return n
    res = 0
    i = 1
    while i <= m and i <= n:
        res += calculate(n - i, m)
        i += 1
    return res


def solve_gen(n, m):
    return calculate(n + 1, m)

if __name__ == '__main__':
    basamak = 4
    adim = 2
    print(solve_gen(basamak, adim))
