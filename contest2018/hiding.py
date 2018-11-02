from queue import Queue
from string import ascii_lowercase

def move(node):
    neighbors = []
    i, j = node
    if i > 1:
        if j > 0:
            neighbors.append((i - 2, j - 1))
        if j < 14:
            neighbors.append((i - 2, j + 1))
    if i > 0:
        if j > 1:
            neighbors.append((i - 1, j - 2))
        if j < 13:
            neighbors.append((i - 1, j + 2))
    if i < 13:
        if j > 0:
            neighbors.append((i + 2, j - 1))
        if j < 14:
            neighbors.append((i + 2, j + 1))
    if i < 14:
        if j > 1:
            neighbors.append((i + 1, j - 2))
        if j < 13:
            neighbors.append((i + 1, j + 2))

    return neighbors


board = [[10] * 15 for _ in range(15)]
board[7][7] = 0

visited = [[False] * 15 for _ in range(15)]
visited[7][7] = True
q = Queue()
q.put((7, 7))

while not q.empty():
    i, j = q.get()
    num = board[i][j]
    for new_i, new_j in move((i, j)):
        if not visited[new_i][new_j]:
            visited[new_i][new_j] = True
            board[new_i][new_j] = num + 1
            q.put((new_i, new_j))

cases = int(input())
for case in range(cases):
    c, r = input()
    r = 8 - int(r)
    c = ascii_lowercase.index(c)
    max_step = 0
    square = [(7, 7)]

    for i in range(8):
        for j in range(8):
            steps = board[i - r + 7][j - c + 7]
            if steps > max_step:
                max_step = steps
                square = [(i, j)]
            elif steps == max_step:
                square.append((i, j))
    
    print(max_step, end=" ")
    for i, j in square:
        print(ascii_lowercase[j] + str(8 - i), end=" ")
    print()
