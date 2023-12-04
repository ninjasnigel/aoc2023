with open("day4/data.aoc", "r") as file: 
    data = [line.strip("\n") for line in file.readlines()]

total = 0
for line in data:
    line = line.split(":")[1]
    card, winning = line.split("|")
    card, winning = card.split(" "), winning.split(" ")
    points = 0.5
    for number in [x for x in card if x]:
        if number in winning:
            points = points*2
    if points != 0.5:
        total += points
    
cards = 0

def check_win(amount_to_check, start):
    cards = 1
    won_amount = 0
    if amount_to_check == 0:
        return 0
    loop_to = start + amount_to_check
    if loop_to > len(data):
        loop_to = len(data)
    for i in range(start, loop_to):
        won_amount = check_line(data[i])
        for j in range(i+1, i+won_amount+1):
            cards += check_win(1, j)

    return cards

def check_line(line):
    won = 0
    line = line.split(":")[1]
    card, winning = line.split("|")
    card, winning = card.split(" "), winning.split(" ")
    for number in [x for x in card if x]:
        if number in winning:
            won += 1
    return won

for i in range(len(data)):
    total += check_win(1, i)

#jfc i had the correct answer but spent so much fucking time before realizing that i forgot to count the og cards
print(len(data) - 1 + check_win(len(data), 0))