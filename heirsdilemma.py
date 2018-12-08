from collections import Counter

a, b = map(int, input().split())
count = 0

for num in range(a, b+1):
    digits = set([0])
    copy = num
    while copy > 0:
        digit = copy % 10
        if digit in digits or num % digit != 0:
            break
        else:
            digits.add(digit)
            copy = copy // 10
    
    if copy == 0:
        count +=1

print(count)
