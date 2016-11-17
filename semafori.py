def inp():
    num_traffic, road = [eval(data) for data in input().split()]
    traffics = []
    for i in range(num_traffic):
        d, r, g = [eval(data) for data in input().split()]
        traffics.append((d, r, g))
    return road, traffics


def main():
    road, traffics = inp()
    current_d = 0
    time = 0
    for traffic in traffics:
        d, r, g = traffic
        time += d - current_d
        current_d = d
        if (time % (r + g)) <= r:
            time += r - (time % (r + g))
    time += road - current_d
    return time


if __name__ == '__main__':
    print(main())
