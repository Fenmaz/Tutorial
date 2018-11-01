import sys, queue


def inp():
    n = int(sys.stdin.readline()[:-1])
    data = []
    for i in range(n):
        x, y = map(int, sys.stdin.readline().split())
        maze = []
        for line in range(y):
            maze.append(list(sys.stdin.readline()[:-1]))
        data.append(maze)
    return data


def count_a(maze):
    total = 0
    for line in maze:
        total += line.count("A")
    return total


def find_s(maze):
    for i in range(len(maze)):
        if "S" in maze[i]:
            return (i, maze[i].index("S"))


def solve(maze):
    a = count_a(maze)
    x, y = find_s(maze)
    print(a)
    print(x, y)
    q = queue.Queue()

    def find_nex(S):
        nonlocal q, maze
        for borg_i in range(len(S)):
            x, y = S[borg_i]
            n, s, e, w = (x-1, y), (x+1, y), (x, y+1), (x, y-1)
            for step in [n, s, e, w]:
                nex_spot = maze[step[0]][step[1]]
                if nex_spot == "A":
                    maze[step[0]][step[1]] = " ";
                    S_cp = list(S)
                    S_cp[borg_i] = step
                    S_cp.append(step)
                    print("Found an A in small function")
                    print("Returning " + str((tuple(S_cp), found + 1)))
                    return (tuple(S_cp), found + 1)
                elif nex_spot == " ":
                    S_cp = list(S)
                    S_cp[borg_i] = step
                    q.put((tuple(S_cp), found))

    q.put((((x,y), (x,y)), 0))
    q.put((None, None))
    depth = 0
    visited = set(((x,y), (x,y)))
    while not q.empty():
        print("At depth " + str(depth))
        S, found = q.get()
        print("S = " + str(S))
        if found == a:
            return depth
        if S is None:
            depth += 1
            print("\n")
            q.put((None, None))
        elif S not in visited:
            visited.add(S)
            nex = find_nex(S)
            if nex is not None:
                print("Found an A in outer function")
                print("nex = " + str(nex))
                q = queue.Queue()
                q.put(nex)
                q.put((None, None))



def main():
    mazes = inp()
    for maze in mazes:
        print(maze)
        print(solve(maze))


main()

