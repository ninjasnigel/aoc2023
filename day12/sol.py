from functools import lru_cache
import concurrent.futures
import copy

with open("day12/data.aoc", "r") as file: 
    data = [line.strip("\n") for line in file.readlines()]

def parse_list(string):
    return tuple(map(int, string.split(",")))

def format_data(data):
    entries = []
    for entry in data:
        space, springs = entry.split(" ")
        springs = parse_list(springs)
        entries.append((space, springs))
    return entries

def sol1(data):
    entries = format_data(data)
    combinations = 0
    for entry in entries:
        curr_comb = solve_recu(entry)
        combinations += curr_comb
    return combinations

@lru_cache(maxsize=None)
def solve_recu(entry):
    space, springs = entry
    if not springs:
        if space:
            if '#' in space: return 0
        return 1
    elif not space:
        return 0
    combinations = 0
    for i in range(len(space)):
        if '#' in space[0:i]:
            break
        space_taken = i + springs[0]
        if space_taken <= len(space):
            if fits(space[i:], springs[0]):
                combinations += solve_recu((space[i+1+springs[0]:], tuple(springs[1:])))
    return combinations

def fits(space, spring):
    if len(space) < spring: 
        return False
    else:
        c_1 = '.' not in space[0:spring]
        c_2 = True
        if len(space) >= spring+1:
            c_2 = space[spring] != '#'
        condition = c_1 and c_2
        return condition

def unfold(entries):
    new_entries = []
    for entry in entries:
        space, springs = entry
        new_space, new_springs = space, copy.copy(springs)
        for i in range(4):
            new_space += '?' + space
            new_springs += springs
        new_entries.append([new_space, new_springs])
    return new_entries

def process_entry(entry):
    return solve_recu((entry[0], tuple(entry[1])))

def sol2(data):
    entries = format_data(data)
    unfolded_entries = unfold(entries)
    total_entries = len(unfolded_entries)
    combinations = 0
    # Even when multithreading on 16 cores it doesn't take feasable time
    # after 5 minutes it had solved like 10% of the total entries
    # and it was slowing down the further it went

    # Using caching made execute almost instantly
    # Very good lesson on how caching can help in recursive functions
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = {executor.submit(process_entry, entry): entry for entry in unfolded_entries}
        for i, future in enumerate(concurrent.futures.as_completed(futures)):
            try:
                result = future.result()
                combinations += result
                print(f'Completed {i + 1} out of {total_entries}')
            except Exception as exc:
                print(f'Generated an exception: {exc}')
    return combinations

if __name__ == "__main__":
    print('Total arrangements sol1: ', sol1(data))
    print('Total arrangements sol2: ', sol2(data))