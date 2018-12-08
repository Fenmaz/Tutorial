import math

phi = (1 + math.sqrt(5)) / 2
psi = (1 - math.sqrt(5)) / 2

def fib(n):
    return math.pow(phi, n) / math.sqrt(5)

print(round(fib(10 ** 4) % (10 ** 9)))
