import sys


def inp():
    first_l = sys.stdin.readline().split()
    first_l = list(map(int, first_l))
    data = sys.stdin.readline().split()
    data = list(map(int, data))
    return first_l, data


def main(h, w, n, data):
    data.reverse()
    for i in range (h):
        remain = w
        while remain > 0 and data:
            b = data.pop()
            remain -= b
        if remain != 0:
            return "NO"
    return "YES"


in1, in2 = inp()
print(main(*in1, in2))

