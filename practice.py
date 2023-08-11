import sys

input = sys.stdin.readline

n = int(input())


def pibonachi(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return pibonachi(n - 1) + pibonachi(n - 2)


print(pibonachi(n))
