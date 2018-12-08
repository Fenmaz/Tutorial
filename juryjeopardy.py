cases = int(input())
print(cases)

# direction: East is (1, 0); South is (0, 1).
def turn(face, direction):
    if direction == "B":
        face[0], face[1] = -face[0], -face[1]
    elif direction == "R":
        face[0], face[1] = -face[1], face[0]
    elif direction == "L":
        face[0], face[1] = face[1], -face[0]
    return face
 
    
for _ in range(cases):
    face = [1, 0]
    pos = (0, 0)
    open = set([pos])
    for step in input():
        face = turn(face, step)
        pos = (pos[0] + face[0], pos[1] + face[1])
        open.add(tuple(pos))
    max_x = max(open)[0]
    min_y = min(open, key=lambda x: x[1])[1]
    max_y = max(open, key=lambda x: x[1])[1]
    print(max_y - min_y + 3, end=" ")
    print(max_x + 2)
    print("#" * (max_x + 2))
    for row in range(min_y, max_y + 1):
        for col in range(max_x + 2):
            if (col, row) in open:
                print(".", end="")
            else:
                print("#", end="")
        print()
    print("#" * (max_x + 2))
