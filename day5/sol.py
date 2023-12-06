from concurrent.futures import ThreadPoolExecutor
with open("day5/data.aoc", "r") as file: 
    data = [line.strip("\n") for line in file.readlines()]

import os
import win32api
import win32process
import win32con

def set_high_priority():
    handle = win32api.OpenProcess(win32con.PROCESS_ALL_ACCESS, True, os.getpid())
    win32process.SetPriorityClass(handle, win32process.HIGH_PRIORITY_CLASS) # you could set this to REALTIME_PRIORITY_CLASS etc.

set_high_priority()

new_data = []
temp_data = []
#Proccess data
for line in data[2:]:
    if not line:
        new_data.append(temp_data)
        temp_data = []
    elif line[0].isdigit():
        temp_data.append(line.split(" "))
    if(line == data[-1]):
        new_data.append(temp_data)
        temp_data = []

initial_seeds = [int(x) for x in data[0].split(":")[1].split(" ") if x]

seed_ranges = []
for i in range(0, len(initial_seeds), 2):
    seed_ranges += [(initial_seeds[i], initial_seeds[i+1])]

seeds = []
for map in new_data:
    map_type = []
    for line in map:
        map_type += [(int(line[1]), int(line[1]) + int(line[2]) -1, int(line[0]) - int(line[1]))]
    seeds += [map_type]

def get_corresponding(seed, map):
    for seed_map in map:
        if seed <= seed_map[1] and seed >= seed_map[0]:
            if seed + seed_map[2] == 2: print(seed_map, "|", seed)
            return seed + seed_map[2]
    return seed


final_seeds = []
for seed in initial_seeds:
    for map_type in seeds:
        seed = get_corresponding(seed, map_type)
    final_seeds += [seed]

print(min(final_seeds))

final_seeds = []
for seed_pair in seed_ranges:
    print(seed_pair)
    for seed in range(seed_pair[0], seed_pair[0] + seed_pair[1]):
        for map_type in seeds:
            seed = get_corresponding(seed, map_type)
        final_seeds += [seed]

print(min(final_seeds))