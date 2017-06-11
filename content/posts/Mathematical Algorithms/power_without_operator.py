def nested_pow(a, b):
    if b == 0:
        return 1
    result, increment = a, a
    for i in range(1, b):
        for j in range(1, a):
            result += increment
        increment = result
    return result


def recursion_pow(a, b):
    if b != 0:
        return multiply(a, recursion_pow(a, b - 1))
    else:
        return 1


def multiply(x, y):
    if y != 0:
        return x + multiply(x, y - 1)
    else:
        return 0

if __name__ == '__main__':
    print(nested_pow(5, 6))
    print(recursion_pow(5, 3))
