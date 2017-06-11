def adjust(l, score, n):
    for i in range(score, n + 1):
        l[i] += l[i - score]


def count(n):
    result = [0] * (n + 1)
    result[0] = 1  # 0 puan için

    adjust(result, 3, n)
    adjust(result, 5, n)
    adjust(result, 10, n)

    return result[n]


def count_new(n):
    result = [0] * (n + 1)
    result[0] = 1  # 0 puan için

    for i in range(3, n + 1):
        if i >= 3:
            result[i] += result[i - 3]
        if i >= 5:
            result[i] += result[i - 5]
        if i >= 10:
            result[i] += result[i - 10]

    return result[n]

if __name__ == '__main__':
    score = 13
    print(count_new(score))
