def recursion(n):
    if n <= 1:
        return n
    return recursion(n - 1) + recursion(n - 2)


def dynamic(n):
    fib_list = [0, 1]
    for i in range(2, n + 1):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])
    return fib_list[n]


def space_dynamic(n):
    a, b = 0, 1
    if n == 0:
        return a
    for i in range(2, n + 1):
        a, b = b, a + b
    return b


def matrix(n):
    F = [[1, 1], [1, 0]]
    if not n:
        return 0
    power(F, n - 1)
    return F[0][0]


def matrix_opt(n):
    F = [[1, 1], [1, 0]]
    if not n:
        return 0
    power(F, n - 1)
    return F[0][0]


def power(F, n):
    M = [[1, 1], [1, 0]]
    for i in range(2, n + 1):
        multiply(F, M)


def power_opt(F, n):
    if n == 0 and n == 1:
        return
    M = [[1, 1], [1, 0]]
    power_opt(F, n / 2)
    multiply(F, F)
    if n % 2 != 0:
        multiply(F, M)


def multiply(F, M):
    x = F[0][0] * M[0][0] + F[0][1] * M[1][0]
    y = F[0][0] * M[0][1] + F[0][1] * M[1][1]
    z = F[1][0] * M[0][0] + F[1][1] * M[1][0]
    w = F[1][0] * M[0][1] + F[1][1] * M[1][1]

    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w

if __name__ == '__main__':
    n = 9
    print(recursion(n))
    print(dynamic(n))
    print(space_dynamic(n))
    print(matrix(n))
    print(matrix_opt(n))
