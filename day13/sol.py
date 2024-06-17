with open("day13/data.aoc", "r") as file: 
    data = [line.strip("\n") for line in file.readlines()]

def transpose(data):
    return list(map(list, zip(*data)))

def format_data(data):
    new_data = []
    actual_data = []
    for row in data:
        if row == '':
            actual_data.append(new_data)
            new_data = []
            continue
        new_data.append(list(row))
    actual_data.append(new_data)
    return actual_data

def mirror_score(data, use_smudge=False):
    data_x = format_data(data)
    symmetrical_value = 0
    for area in data_x:
        horizontal = find_reflections(area, use_smudge=use_smudge)
        vertical = find_reflections(transpose(area), use_smudge=use_smudge)
        symmetrical_value += 100*horizontal +vertical
    return symmetrical_value

def find_reflections(area, use_smudge=False):
    symmetrical = 0
    for i in range(0, len(area) - 1):
        smudge_used = False
        if not smudge_used and use_smudge:
            smudge_used = smudged(area[i], area[i + 1])
        if area[i] == area[i + 1] or smudge_used:
            for j in range(0, len(area)):
                if i - j - 1 == -1 or j + i + 2 >= len(area):
                    if(use_smudge):
                        if smudge_used: symmetrical = i+1
                    else: symmetrical = i+1
                    break
                elif not smudge_used and use_smudge:
                    if smudged(area[i - j - 1], area[i + j + 2]):
                        smudge_used = True
                    elif area[i - j - 1] != area[i + j + 2]:
                                        break
                elif area[i - j - 1] != area[i + j + 2]:
                    break
    return symmetrical

def smudged(line1, line2):
    return sum([1 for i in range(len(line1)) if line1[i] != line2[i]]) == 1

# --------------- sol2 ----------------

def sol1(data):
    return mirror_score(data, use_smudge=False)

def sol2(data):
    return mirror_score(data, use_smudge=True)

print(sol1(data))
print(sol2(data))