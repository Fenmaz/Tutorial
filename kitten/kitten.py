import sys

def inp():
    stuck = input()
    data = {}
    for line in sys.stdin:
        line_split = line.split()
        if line_split[0] != "-1":
            low_branch = line_split[0]
            for up_branch in line_split[1:]:
                data[up_branch] = low_branch
    return (stuck, data)


def main(stuck, data):
    res = stuck + " "
    while stuck in data:
        stuck = data[stuck]
        res += stuck + " "
    return res[:-1]

s, d = inp()
print(main(s, d))

