def find_next(num):
    for i in range(len(num) - 1, 0, -1):
        if num[i] > num[i - 1]:
            break

    if i - 1 == 0:
        print("Imkansiz")
        return

    x, smallest = num[i - 1], i
    for j in range(i + 1, len(num)):
        if num[j] > x and num[j] < num[smallest]:
            smallest = j

    num = list(num)
    num[smallest], num[i - 1] = num[i - 1], num[smallest]

    num[i:] = sorted(num[i:])
    print(''.join(num))

if __name__ == '__main__':
    find_next("534976")
    find_next("4321")
