import math


def max_lenght(previous, next, weight):
    if previous != 1:
        if abs(previous - next) > previous:
            return math.sqrt(weight ** 2 + (previous - next) ** 2)
        else:
            return math.sqrt(weight ** 2 + (previous - 1) ** 2)
    else:
        if previous >= next:
            return math.sqrt(weight ** 2 + (previous - 1) ** 2)
        else:
            return math.sqrt(weight ** 2 + (next - 1) ** 2)


def get_the_worst(file):
    with open(file) as f:
        w = int(f.readline())
        for line in f.readlines():
            heights = line.split(" ")
            h = []
            for i in range(len(heights)):
                h.append(int(heights[i]))
    print(h)
    sum = 0
    l = len(h)
    for i in range(l - 1):
        sum += max_lenght(h[i], h[i + 1], w)
    return round(sum, 2)
