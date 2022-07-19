import math


def square(n):
    val = (int(math.sqrt(n)))
    if val * val == n:
        print(True)


square(655363)
