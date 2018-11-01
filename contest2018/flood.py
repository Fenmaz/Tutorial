from collections import Counter

cases = int(input())

for _ in range(cases):
    table = []
    n = int(input())
    for line in range(n):
        new_line = list(map(int, input()))
        table.append(new_line)

    count = 0
    c = [0] * 6
    new = [[]] * 6
    connected = set()
    connected.add(tuple([0, 0]))
    while len(connected) != n*n:
        #print(connected)
        count += 1
        for tile in connected:
            print(tile)
            if tile[0] > 0 and tuple([tile[0] - 1, tile[1]]) not in connected:
                new[table[tile[0] - 1][tile[1]]].append(tuple([tile[0] - 1, tile[1]]))
            if tile[0] < n and tuple([tile[0] + 1, tile[1]]) not in connected:
                #print(table[tile[0] + 1][tile[1]])
                new[table[tile[0] + 1][tile[1]]].append(tuple([tile[0] + 1, tile[1]]))
            if tile[1] > 0 and tuple(tile[0], tile[1] - 1) not in connected:
                new[table[tile[0]][tile[1] - 1]].append(tuple([tile[0], tile[1] - 1]))
            if tile[1] < n and tuple(tile[0], tile[1] + 1) not in connected:
                new[table[tile[0]][tile[1] + 1]].append(tuple([tile[0], tile[1] + 1]))
        count_new = tuple(map(len, new))
        max_new = max(count_new)
        choice = count_new.index(max)
        c[choice] += 1
        connected.update(new[choice])
    print(count)
    print(c)
    