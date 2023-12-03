import re

with open("day3/data.aoc", "r") as file: 
    data = [line.strip("\n") for line in file.readlines()]

symbols = ['*', '#', '+', '$', '%', '&', '!', '?', '@', '^', '~', '`', '>', '<', '(', ')', '[', ']', '{', '}', '|', '/', '\\', '-', '_', '=', '+', ':', ';', '"', "'", ',']
get_adjacent = lambda x, y: [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)]

def find_adjacent_symbol(x, y):
    for adjacent_x, adjacent_y in get_adjacent(x, y):
        if 0 <= adjacent_x < len(data) and 0 <= adjacent_y < len(data[adjacent_x]):
            if data[adjacent_x][adjacent_y] in symbols:
                return adjacent_x, adjacent_y
    return None

numbers = {}
for line_index, line in enumerate(data):
    num_index = [-1, -1]
    for row_index, char in enumerate(line):
        if char.isdigit() and num_index != [-1, -1]:
            num_index[1] += 1
            if row_index + 1 >= len(line) or not line[row_index+1].isdigit():
                num_index[1] += 1
                numbers[(line_index, num_index[0], num_index[1])] = (int(line[num_index[0]:num_index[1]]))
                num_index = [-1, -1]
        elif char.isdigit():
            num_index[0], num_index[1]  = row_index, row_index
            if row_index + 1 >= len(line) or not line[row_index+1].isdigit():
                num_index[1] += 1
                numbers[(line_index, num_index[0], num_index[1])] = (int(line[num_index[0]:num_index[1]]))
                num_index = [-1, -1]

sum = 0
mulsum = 0
pairs = {}
for key in numbers:
    for x_value in range(key[1],key[2]):
        adjecent = find_adjacent_symbol(int(key[0]), x_value)
        if adjecent:
            sum += numbers[key]
            #sol2
            if data[adjecent[0]][adjecent[1]] == "*":
                get_adjacent(adjecent[0], adjecent[1])
                for char in get_adjacent(adjecent[0], adjecent[1]):
                    if data[char[0]][char[1]].isdigit():
                        number = data[char[0]][char[1]]
                        for index in range(char[1]+1, len(data[char[0]])):
                            if not data[char[0]][index].isdigit():
                                break
                            else:
                                number += data[char[0]][index]
                        for index in range(char[1]-1, -1, -1):
                            if not data[char[0]][index].isdigit():
                                break
                            else:
                                number = data[char[0]][index] + number
                        if int(number) != numbers[key] and (int(number), numbers[key]) not in pairs and (numbers[key], int(number)) not in pairs:
                            pairs[adjecent] = (int(number), numbers[key])
                            break
            break

for gear, values in pairs.items():
    mulsum += values[0] * values[1]

print("sol1", mulsum)
print("sol2", sum)