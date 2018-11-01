import sys

sys.setrecursionlimit(3000)


def inp():
    data = []
    for line in sys.stdin:
        data.append(line)

    dim = [int(i) for i in data[0].split(" ")]
    grid = {}
    player = ()
    for i in range(dim[1]):
        for j in range(dim[0]):
            char = data[i + 1][j]
            if char == "#":
                grid[i, j] = 1
            elif char == ".":
                grid[i, j] = 2
            elif char == "G":
                grid[i, j] = 3
            elif char == "T":
                grid[i, j] = 4
            elif char == "P":
                player = (i, j)
                grid[i, j] = 2
    return grid, player


def gold(grid, player):
    # Code:
    # 0 - visited   1 - wall
    # 2 - empty     3 - gold
    # 4 - trap
    count = 0

    def test_trap(x, y):
        if grid[x, y+1] == 4 or grid[x+1, y] == 4 or grid[x-1, y] == 4 or grid[x, y-1] == 4:
            return True
        return False

    def dfs(x, y):
        # print(x, y)
        nonlocal count
        if grid[x, y] == 3:
            count += 1
            grid[x, y] = 2
        if grid[x, y] == 2:
            grid[x, y] = 0
            if not test_trap(x, y):
                dfs(x, y+1)
                dfs(x+1, y)
                dfs(x-1, y)
                dfs(x, y-1)

    dfs(*player)
    return count


def main():
    g, p = inp()
    print(gold(g, p))


if __name__ == '__main__':
    main()

