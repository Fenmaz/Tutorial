from sys import stdin

def dfs(seen, movable, node):
    stack = [node]
    while stack:
        next = stack.pop()
        if next not in seen:
            seen.add(next)
            for neighbor in adj(next):
                if neighbor in movable:
                    stack.append(neighbor)

def adj(node):
    i, j = node
    return [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
                    
line = stdin.readline()
case = 1
while line:
    m, n = map(int, line.strip().split())
    white = set()
    for i in range(m):
        l = stdin.readline().strip()
        for j in range(n):
            if l[j] == "-":
                white.add((i, j))
    
    seen = set()
    count = 0
    for i in range(m):
        for j in range(n):
            node = (i, j)
            if node in white and node not in seen:
                dfs(seen, white, node)
                count += 1
    
    print("Case", end=" ")
    print(case, end=": ")
    print(count)
    
    line = stdin.readline()
    case += 1
    