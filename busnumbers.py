def inp():
    _ = input()
    buses = [eval(bus) for bus in input().split()]
    return buses


def main():
    buses = inp()
    buses.sort()
