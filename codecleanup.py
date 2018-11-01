n = int(input())
cleanup_days = input().split()
cleans = 0
dirty_pushes = 0
dirtiness = 0

for i in range(1, 366):
    if dirtiness >= 20:
        dirty_pushes = 0
        dirtiness = 0
        cleans += 1
        print(i)
    if str(i) in cleanup_days:
        dirty_pushes += 1
    dirtiness += dirty_pushes
if dirtiness > 0:
    cleans += 1
print(cleans)