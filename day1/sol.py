nums = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
get_num = lambda s, i: next((nums.get(s[i:i+l]) for l in (3, 4, 5) if i + l <= len(s) and s[i:i+l] in nums), '')

#sol1
with open("day1/data.aoc", "r") as file: 
    total_sum = sum([int(n[0] + n[-1]) for n in \
                ["".join(c for c in line if c.isdigit()) for line in file.readlines()]]); print(total_sum)

#sol2
with open("day1/data.aoc", "r") as file: 
    total_sum = sum([int(n[0] + n[-1]) for n in ["".join(str(c) if c.isdigit() else \
                str(get_num(line, i)) for i, c in enumerate(line)) for line in file.readlines()]]); print(total_sum)