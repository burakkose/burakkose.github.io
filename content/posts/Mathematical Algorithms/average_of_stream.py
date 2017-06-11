def get_avg(prev, num, count):
    return (prev * count + num) / (count + 1)


def calculate_stream(arr):
    avg = 0
    for i, num in enumerate(arr):
        avg = get_avg(avg, num, i)
        print(num, " geldiğinde ortalama = ", avg, sep="")

if __name__ == '__main__':
    arr = [10, 20, 30, 40, 50, 60]
    calculate_stream(arr)
