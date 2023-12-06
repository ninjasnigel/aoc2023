with open("day4/data.aoc", "r") as file: 
    data = [line.strip("\n") for line in file.readlines()]

cards = []
#Proccess data
for line in [line for line in data if line]:
    line = line.split(":")[1]
    card, winning = line.split("|")
    card, winning = card.split(" "), winning.split(" ")
    cards.append((card, winning))

#Calculate points
total = 0
for card in cards:
    points = 0.5
    for number in [x for x in card[0] if x]:
        if number in card[1]:
            points = points*2
    if points != 0.5:
        total += points
print(total)

def revurv_win_check(start_index):
    card_amount = 1
    wins = 0
    loop_to = start_index+1+wins
    for number in cards[start_index][0]:
        if number in cards[start_index][1]:
            wins += 1
    if start_index+1+wins > len(cards):
        loop_to = len(cards)
    for i in range(start_index+1, loop_to):
        card_amount += revurv_win_check(i)
    return card_amount

card_amount = 0
for i in range(len(cards)):
    card_amount += revurv_win_check(i)

print(card_amount)