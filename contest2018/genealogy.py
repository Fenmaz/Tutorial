command = ''
ancestry = dict()

def birth(params_str):
    data = params_str.split(' : ')
    ancestry[data[0]] = {'birth': data[1], 'parents': data[2:3], 'children': []}

def death(params_str):
    data = params_str.split(' : ')
    ancestry[data[0]]['death'] = data[1]

def get_parents(n):
    if not ancestry[n]['parents']:
        return None
    else:
        n_parents = ancestry[n]['parents']
    
    indents += 2

    for parent in n_parents:
        if 'birth' in ancestry[parent]:
            s += indents*' '  + f'{parent} {ancestry[parent]['birth']} - {ancestry[parent].get('death', default=''} \n'
        else:
            s += f'{parent} \n'
        get_parents(parent)

while command != 'QUIT':
    command_str = input()
    command = command_str.split(' ')[0]
    
    if command == 'BIRTH':
        params = command_str[6:]
        birth(params)
    if command == 'DEATH':
        params = command_str[6:]
        death(params)
    if command == 'ANCESTRY':
        name = command_str[10:].split(' : ')
        indents = 0
        s = 'ANCESTORS of ' + name + '\n'
        get_parents(name)
print(ancestry)

