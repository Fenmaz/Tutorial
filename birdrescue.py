n, q = map(int, input().split())

x0, y0 = map(int, input().split())

birds = []

for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    in_x = (x1 >= x0 and x2 <= x0) or (x1 <= x0 and x2 >= x0)
    in_y = (y1 >= y0 and y2 <= y0) or (y1 <= y0 and y2 >= y0)
    
    x1, y1, x2, y2 = map(abs, (x1 - x0, y1 - y0, x2 - x0, y2 - y0))

    if in_x and in_y:
        lo = 0
    elif in_x:
        lo = min(y1, y2)
    elif in_y:
        lo = min(x1, x2)
    else:
        lo = min(x1, x2) + min(y1, y2)
    
    hi = max(x1, x2) + max(y1, y2)
    
    birds.append((lo, hi))

#birds.sort()

from collections import Counter
calls = []
count = Counter()

for i in range(q):
    #call = int(input())
    #count = 0
    #for lo, hi in birds:
    #    if lo > call:
    #        break
    #    if hi >= call:
    #        count += 1
    #print(count)
    
    calls.append(int(input()))
    
#for lo, hi in birds:
    