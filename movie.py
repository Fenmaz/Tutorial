cases = int(input())

for _ in range(cases):
    m, r = map(int, input())
    stack = [i for i in range(m)]
    requests = map(int, input())
    
    for request in requests:
        for i, movie in enumerate(stack):
            if movie == request:
                for k in range(i, 0, -1):
                    stack[k], stack[k-1] = stack[k-1], stack[k]
