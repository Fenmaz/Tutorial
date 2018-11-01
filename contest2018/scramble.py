from string import ascii_lowercase
ascii_lowercase = ' ' + ascii_lowercase
trials = int(input())

def convert_to_num(s):
    num_list = []
    for letter in s:
        num_list.append(ascii_lowercase.index(letter))
    return num_list

def convert_to_str(n):
    str_list = ''
    for num in n:
        str_list += ascii_lowercase[num]
    return str_list

def encrypt(s):
    l = convert_to_num(s)
    for i in range(len(l))[1:]:
        l[i] = (l[i - 1] + l[i]) % 27
    return l

def decrypt(s):
    l = convert_to_num(s)
    real = [l[0]]
    for i in range(len(l))[1:]:
        if l[i] >= l[i-1]:
            real.append(l[i] - l[i-1])
        else:
            real.append(l[i] + 27 - l[i-1])

    return real

for t in range(trials):
    trial = input()
    task = trial[0]
    s = trial[2:]

    if task == 'e':
        print(convert_to_str(encrypt(s)))
    else:
        print(convert_to_str(decrypt(s)))
    

