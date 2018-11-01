def adj(node):
    neighbors = []
    i, j = node
    if i > 0:
        neighbors.append((i - 1, j))
    if i < r - 1:
        neighbors.append((i + 1, j))
    if j > 0:
        neighbors.append((i, j - 1))
    if j < c - 1:
        neighbors.append((i, j + 1))
    return neighbors


r, c = map(int, input().split())
land = set()
cloud = set()

for i in range(r):
    for j, char in enumerate(input()):
        if char == "L":
            land.add((i, j))
        elif char == "C":
            cloud.add((i, j))

visited = set()
counter = 0

for node in land:
    if node not in visited:
        visited.add(node)
        stack = adj(node)
        while stack:
            node = stack.pop()
            if (node in land or node in cloud) and node not in visited:
                visited.add(node)
                stack.extend(adj(node))
        counter += 1

print(counter)
