def deg(s):
    for i in range(len(s) - 1, 0, -1):
        seen = set()
        dup = set()
        for j in range(len(s) - i + 1):
            sub = s[j: j + i]
            if sub in seen:
                dup.add(sub)
            else:
                seen.add(sub)
        if dup == seen:
            return i
    return 0
    
from sys import stdin
for line in stdin:
    print(deg(line.strip()))
