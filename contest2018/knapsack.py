import sys

def knapsack(cap, items):
    best = [[0] * (len(items) + 1) for _ in range(cap + 1)]
    for w in range(1, cap + 1):
        for i, (value, weight) in enumerate(items):
            if weight > w:
                best[w][i+1] = best[w][i]
            else:
                best[w][i+1] = max(best[w][i], value + best[w - weight][i])

    weight = cap
    last_item = len(items)
    choice = []
    while best[weight][last_item] > 0:
        if best[weight][last_item] != best[weight][last_item - 1]:
            weight -= items[last_item - 1][1]
            choice.append(last_item - 1)
        else:
            last_item -= 1
    return choice


line = sys.stdin.readline()
while line:
    cap, n = line.split()
    n = int(n)
    cap = int(float(cap))
    items = []
    for _ in range(n):
        line = sys.stdin.readline()
        items.append(tuple(map(int, line.split())))
    choice = knapsack(cap, items)

    print(len(choice))
    for item in choice:
        print(item, end=" ")
    print()

    line = sys.stdin.readline()
