import math


def hypotenuse(height_array, width):
    return math.sqrt(width ** 2 + height_array ** 2)


def solution(previous, next):
    bigger = previous
    if next > previous:
        bigger = next
    return max(bigger - 1, abs(previous - next))


def get_the_worst(file):
    with open(file) as f:
        width = int(f.readline())
        for line in f.readlines():
            heights = line.split(" ")
            height_array = []
            for i in range(len(heights)):
                height_array.append(int(heights[i]))
    sum = 0
    l = len(height_array)
    for i in range(l - 1):
        sum += hypotenuse(solution(height_array[i], height_array[i + 1]), width)
    return round(sum, 2)