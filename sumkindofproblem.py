# 1 + 2 + 3 + ... + n = n(n+1)/2
# 2 + 4 + 6 + ... + 2n = 2 * (1 + 2 + 3 + ... + n) = n(n+1)
# 1 + 3 + 5 + ... + (2n - 1) = n(n+1) - n = n^2

cases = int(input())

for case in range(cases):
    i, n = map(int, input().split())
    even = n * (n + 1)
    odd = even - n
    pos = even // 2
    print(str(i) + " " + str(pos) + " " + str(odd) + " " + str(even))
