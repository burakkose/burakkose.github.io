MONEY = (1, 2, 5, 10, 20, 50, 100, 200)


def find_min(target):
    result = []
    for m in sorted(MONEY, reverse=True):
        while target >= m:
            target -= m
            result.append(m)
    print(*result, sep=" Tl + ", end=" = {} TL".format(sum(result)))

if __name__ == '__main__':
    target = 1994
    find_min(target)
