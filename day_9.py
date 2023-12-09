def format_data(raw):
    new_data = []
    fixed_data = raw.strip(" ").strip("\n").split("\n")
    for line in fixed_data:
        new_data.append(line.split(" "))
    return new_data, new_data

def get_diffs(line):
    diff_line = []
    for i in range((len(line)-1)):
        diff_line += [int(line[i+1]) - int(line[i])]
    return diff_line

def step_one(line):
    step_one = []
    step_one.append([int(number) for number in line])
    while(sum(get_diffs(line)) != 0):
        line = get_diffs(line)
        step_one.append(line)
    step_one.append(get_diffs(line))
    return step_one
   
def star1(data):
    step_ones = []
    sum = 0
    for line in data:
        step_ones.append(step_one(line))
    for i in range(len(step_ones)):
        sequences = step_ones[i]
        sequences.reverse()
        for sequence in sequences:
            sequence.append(0)
        for j in range(1, len(sequences)):
            sequences[j][-1] = sequences[j][-2] + sequences[j-1][-1]
        sum += sequences[-1][-1]
    return sum

def star2(data):
    step_ones = []
    sum = 0
    for line in data:
        step_ones.append(step_one(line))
    for i in range(len(step_ones)):
        sequences = step_ones[i]
        sequences.reverse()
        for sequence in sequences:
            sequence.insert(0, 0)
        for j in range(1, len(sequences)):
            sequences[j][0] = sequences[j][1] - sequences[j-1][0]
        sum += sequences[-1][0]
    return sum

from elis_script import *

if __name__ == '__main__':
    main(format_data, star1, star2) # add year, day if not done on puzzle day