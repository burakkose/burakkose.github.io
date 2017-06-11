def brute1(num, x):
    result = 1
    for i in range(x):
        result *= num
    return result

    def div_conq(num, x):
        if x == 0:
            return 1
        temp = div_conq(num, y / 2)
        if x % 2 == 0:
            return temp * temp
        else:
            return num * temp * temp

if __name__ == '__main__':
