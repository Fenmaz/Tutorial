m = int(input())

n = int(m ** (1/3)) + 1

bus_num = set()
cubed = [0]

largest = -1

for i in range(n+1):
    cubed.append(i ** 3)
    
for i in range(1, n+1):
    for j in range(i, n+1):
        num = cubed[i] + cubed[j]
        if num <= m:
            if num in bus_num and num > largest:
                largest = num
            bus_num.add(num)

if largest != -1:
    print(largest)
else:
    print("none")
