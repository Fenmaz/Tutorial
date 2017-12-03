def inp():
    dna1 = input()
    dna2 = input()
    return dna1, dna2


def main(dna1, dna2):
    first_index = second_index = min(len(dna1), len(dna2))

    for i, (a, b) in enumerate(zip(dna1, dna2)):
        if a != b:
            first_index = i
            break

    second_index -= first_index
    for i, (a, b) in enumerate(zip(reversed(dna1[first_index:]), reversed(dna2[first_index:]))):
        if a != b:
            second_index = i
            break

    return len(dna2) - first_index - second_index


if __name__ == '__main__':
    print(main(*inp()))
