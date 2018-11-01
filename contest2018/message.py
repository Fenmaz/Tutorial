import copy, sys

file_in = sys.stdin.read()
lines = file_in.splitlines()

x = 0
while x < len(lines): 
    first_person, last_person = lines[x].split()
    x += 1
    trials = int(lines[x])
    x += 1
    group_list = []

    for i in range(trials):
        group = lines[x].split()
        x += 1
        group_list.append(group)


    def get_min_path(groups, start_person):
        min_risk = 10000000000000000
        min_path = []
        min_person = ''
        for group in groups:
            new_groups = copy.deepcopy(groups)
            new_groups.remove(group)
            group_risk = len(group) - 2
            if start_person in group:
                if last_person in group:
                    if group_risk < min_risk:
                        min_risk = group_risk
                        min_person = last_person
                        min_path = []
                else:
                    for person in group:
                        risk, path = get_min_path(new_groups, person)
                        if risk < min_risk:
                            min_path = path
                            min_risk = risk + group_risk + 1
                            min_person = person
        return (min_risk, [min_person] + min_path)

    risk, path = get_min_path(group_list, first_person)
    if last_person in path:
        print(str(risk), first_person, ' '.join(path))
    else:
        print('impossible')
