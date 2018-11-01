n = int(input())
c = list(map(int, input().split()))

can = True
if sum(c) != 2 * (n - 1):
    can = False
else:
    for i in range(len(c)):
        num = c[i]
        for j in range(len(c) - i - 1):
            if num > 0 and c[i + 1 + j] > 0:
                c[i + j + 1] -= 1
                num -= 1
        if num != 0:
            can = False
        c[i] = num
    if c[-1] != 0:
        can = False

if can:
    print("YES")
else:
    print("NO")