import sys


def inp():
    data = []
    for line in sys.stdin:
        data.append(line)

    names = []
    line_num = 1
    while line_num < len(data):
        num_names = int(data[line_num])
        names.append([data[line_num + i + 1] for i in range(num_names)])
        line_num += num_names + 1
    return names


def find_max_depth(cases):
    max_depth = 0
    for case in cases:
        if len(case[1]) > max_depth:
            max_depth = len(case[1])
    return max_depth


def fill_in_classes(cases, max_depth):
    for case in cases:
        if len(case[1]) < max_depth:
            case[1] += "2" * (max_depth - len(case[1]))
    return cases


def main():
    data = inp()
    for list_of_name in data:
        cases = []
        for line in list_of_name:
            name = line.split(": ")
            name[1] = name[1].replace(" class", "")
            name[1] = name[1].replace("upper", "1")
            name[1] = name[1].replace("middle", "2")
            name[1] = name[1].replace("lower", "3")
            name[1] = name[1].replace("-", "")
            name[1] = name[1].replace("\n", "")
            name[1] = name[1][::-1]
            cases.append(name)
        cases.sort(key=lambda lst: lst[0])
        n = find_max_depth(cases)
        cases = fill_in_classes(cases, n)
        cases.sort(key=lambda lst: lst[1])
        for case in cases:
            print(case[0])
        print("=" * 30)

if __name__ == '__main__':
    main()
