import math


def hypotenuse(h, w):
    return math.sqrt(w ** 2 + h ** 2)


def solution(previous, next):
    bigger = previous
    if next > previous:
        bigger = next
    return max(bigger - 1, abs(previous - next))


def get_the_worst(file):
    with open(file) as f:
        w = int(f.readline())
        for line in f.readlines():
            heights = line.split(" ")
            h = []
            for i in range(len(heights)):
                h.append(int(heights[i]))
    sum = 0
    l = len(h)
    for i in range(l - 1):
        sum += hypotenuse(solution(h[i], h[i + 1]), w)
    return round(sum, 2)