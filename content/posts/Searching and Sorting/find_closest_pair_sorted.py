from math import inf


def print_closest(ar1, ar2, x):
    diff = inf
    res_l, res_r = -1, -1
    l, r = 0, len(ar2) - 1

    while l < len(ar1) and r >= 0:
        if abs(ar1[l] + ar2[r] - x) < diff:
            resl_l, res_r, diff = l, r, abs(ar1[l] + ar2[r] - x)

        if ar1[l] + ar2[r] > x:
            r -= 1
        else:
            l += 1

    print("({} - {})".format(ar1[res_l], ar2[res_r]))

if __name__ == '__main__':
    ar1 = [1, 4, 5, 7]
    ar2 = [10, 20, 30, 40]
    x = 38
    print_closest(ar1, ar2, x)
