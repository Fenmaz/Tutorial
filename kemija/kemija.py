import sys


def inp():
    return sys.stdin.read()[:-1]


def main(s):
    i = 0
    res = []
    while i < len(s):
        res.append(s[i])
        if s[i] in ['a','e','i','o','u']:
            i += 2
        i += 1
    return ''.join(res)

s = inp()
print(main(s))

