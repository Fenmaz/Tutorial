cases = int(input())

for i in range(cases):
    K, n, m, k = map(int, input().split())
    f = [0]
    
    sieve = [True] * (n + 1)
    sieve[0] = False
    for j in range(m, n+1, k):
        sieve[j] = False
    
    for j in range(1, n + 1):
        new = sum(f[j - x] for x in range(1, j) if sieve[x] == True)
        if sieve[j] == True:
            new += 1
        f.append(new)
            
    print(str(K) + " " + str(f[n]))
