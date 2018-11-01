import sys


def inp():
    first_l = sys.stdin.readline()
    num = int(first_l)
    data = []

    def switch(ch):
        return ch == "o"

    for line in sys.stdin.readlines():
        chars = list(line[:-1])
        data.append(list(map(switch, chars)))
    return num, data


def recur_match(lst):
    min = lst.count(True)
    for i in range(10):
        if lst[i] and lst[i+1] and not lst[i+2]:
            lst_c = lst.copy()
            new = recur_match(lst_c_)
            if new < min:
                min = new
    for 

def main(num, data):

