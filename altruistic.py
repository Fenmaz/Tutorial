n, d = map(int, input().split())

frogs = []

for i in range(n):
    frogs.append((i, tuple(map(int, input().split()))))

frogs.sort(key=lambda x: x[1][1], reverse=True)


def combination(limit, height, frogs):
    if frogs is None:
        return set() 

    jump = set()
    for frog in frogs:
        if frog[1][1] < limit and frog[1][0] + height > d:
            jump.add(frog)

    for i, frog in enumerate(frogs):
        jump.update(combination(min(frog[1][1], limit - frog[1][2]), height + frog[1][2], frogs[i+1:]))

    return jump


def solver(frogs):
    jumpable = combination(10 ** 8 + 1, 0, frogs)
    
    if len(jumpable) == 0:
        return n - len(frogs)

    jumped = 0
    for frog in jumpable:
        new_frogs = frogs.copy()
        new_frogs.remove(frog)
        jumped = max(solver(new_frogs), jumped)
    return jumped

print(solver(frogs))
