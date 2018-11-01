from bisect import bisect_left


def inp():
    first_line = input().split(" ")
    num_req, max_req = int(first_line[0]), int(first_line[1])
    timestamps = []
    for i in range(num_req):
        timestamps.append(int(input()))
    return timestamps, max_req


def main():
    timestamps, max_req = inp()
    threshold = 0
    for timestamp in timestamps:
        start = timestamp
        end = timestamp + 1000
        num_req = bisect_left(timestamps, end) - bisect_left(timestamps, start)
        if num_req > threshold:
            threshold = num_req
    return ((threshold - 1) // max_req) + 1


if __name__ == '__main__':
    print(main())
