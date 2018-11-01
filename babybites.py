n = int(input())
bite_l = input().split()

fish = False
for i, bite in enumerate(bite_l):
    if bite != str(i + 1) and bite != "mumble":
        fish = True
        break

if fish:
    print("something is fishy")
else:
    print("makes sense")