import math

def format_data(raw):
    dict_data = {}
    fixed_data = raw.strip(" ").strip("\n").split("\n")
    instructions = []
    for letter in fixed_data[0]:
        if letter == "L": instructions.append(0)
        else: instructions.append(1)
    dict_data['inst'] = instructions
    for i, line in enumerate(fixed_data[2:]):
        dict_data[line.split(" = ")[0]] = (line.split(" = ")[1][1:4], line.split(" = ")[1][6:9], i)
    return dict_data, dict_data

def star1(data):
    curr = 'AAA'
    instructions = data['inst']
    steps = 0
    while curr != 'ZZZ':
        curr_inst = instructions[steps % len(instructions)]
        curr = data[curr][curr_inst]
        steps += 1
    return steps

def star2(data):
    instructions = data['inst']
    curr_keys = [key for key in data.keys() if key.endswith('A')]
    steps = 0
    steps_to_Z = []
    while True:
        curr_inst = instructions[steps % len(instructions)]
        curr_keys = [data[key][curr_inst] for key in curr_keys]
        steps += 1
        for key in curr_keys:
            if key[2] == 'Z':
                steps_to_Z += [steps]
                curr_keys.remove(key)
        if not curr_keys:
            break
    return math.lcm(*steps_to_Z)
from elis_script import *

if __name__ == '__main__':
    main(format_data, star1, star2, 2023, 8) # add year, day if not done on puzzle day