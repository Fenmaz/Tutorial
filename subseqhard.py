import sys
# import random


def inp():
    data = []
    for line in sys.stdin:
        data.append(line)

    seqs_lines = data[3::3]
    seqs_str = [line.replace("\n", "").split(" ") for line in seqs_lines]
    seqs_int = [[int(ele) for ele in seq_str] for seq_str in seqs_str]
    return seqs_int

    # random.seed(0)
    # return [[random.randint(-30, 50) for _ in range(2000)]]


def count_subsequent_sum(seq, num):
    # print(seq)
    # print(num)
    count = 0
    for i in range(len(seq)):
        s = 0
        for j in range(i, len(seq)):
            s += seq[j]
            if s == num:
                count += 1
    return count


def count_subsequent_sum2(seq, num):
    """
    Assume num is prime
    """
    s = [seq[0]]
    for i in range(1, len(seq)):
        s.append(s[-1] + seq[i])

    remainders = dict()
    for ele in s:
        remainders.setdefault(ele % num, []).append(ele // num)

    count = remainders.get(0, []).count(1)
    for lst in remainders.values():
        len_lst = len(lst)
        if len_lst > 1:
            indices = sorted(range(len_lst), key=lambda index: lst[index])
            lst.sort()
            for i in range(len_lst - 1):
                base = lst[i]
                next_index = i + 1
                while lst[next_index] - base < 2:
                    if lst[next_index] - base == 1 and indices[i] < indices[next_index]:
                        count += 1
                    if next_index + 1 < len_lst:
                        next_index += 1
                    else:
                        break
    return count


seqs = inp()
for sequence in seqs:
    print(count_subsequent_sum2(sequence, 47))
