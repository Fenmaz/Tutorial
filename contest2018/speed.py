example = int(input())

while example != -1:
    dist = 0
    last = 0
    for case in range(example):
        spd, time = map(int, input().split())
        dist += spd * (time - last)
        last = time
    print(str(dist) + " miles")
    example = int(input())
