import sys


def inp():
    first_l = sys.stdin.readline()
    data = []
    for line in sys.stdin.readlines():
        data.append(list(line[:-1]))
    return data


def main(data):
    height, width = len(data), len(data[0])
    x, y = 0, 0
    current = data[x][y]
    data[x][y] = 0
    count = 0
    while True:
        if current == "N":
            x -= 1
        elif current == "S":
            x += 1
        elif current == "E":
            y += 1
        elif current == "W":
            y -= 1
        elif current == 0:
            return "Lost"
        elif current == "T":
            return count
        if x in [-1, height] or y in [-1, width]:
            return "Out"
        else:
            current = data[x][y]
            data[x][y] = 0
            count += 1


grid = inp()
print(main(grid))

